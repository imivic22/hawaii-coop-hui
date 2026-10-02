#!/usr/bin/env python3
"""Painted brush-stroke wave band -> SVG.  Standard library only.

Usage: python3 wave_ribbons.py out/wave.svg

Fifteen tapered ribbons ride one shared swell (a big dip-then-crest across the
width plus a secondary ripple).  Each ribbon has its own length, start point,
vertical anchor, phase jitter, amplitude scale and a linear drift whose sign
alternates between strokes so neighbours cross.  Half-width follows
peak * sin(t*pi)^p with mild noise; three strokes break into dry-brush dashes.
"""
import math
import random
import sys

random.seed(7)

W, H = 1400, 320
Y_TOP, Y_BOT = 24.0, 296.0          # the finished composition is remapped into this band
CENTER = 160.0
STEP = 10.0                         # x spacing of samples (px): dense polyline, no corners

TEAL, DEEP, SLATE, INK = '#22a09d', '#0a7473', '#2e6d75', '#113137'
OLIVE, DOLIVE, RUST, TAN = '#8a9140', '#60682d', '#ae562c', '#a5783c'

# ---------------------------------------------------------------- shared swell
L1, L2, L3 = 580.0, 240.0, 120.0   # wavelengths (px)
A1, A2, A3 = 54.0, 8.0, 0.0        # amplitudes (px)
G1 = -2 * math.pi * 50.0 / L1       # pins the big swell: dips near x~400, crests near x~1100
G2 = random.uniform(0, 2 * math.pi)
G3 = random.uniform(0, 2 * math.pi)


def swell(x, s):
    """Shared wave shape with this stroke's phase jitter and amplitude scale."""
    return (A1 * s['amp'] * math.sin(2 * math.pi * x / L1 + G1 + s['j1'])
            + A2 * s['amp'] * math.sin(2 * math.pi * x / L2 + G2 + s['j2'])
            + A3 * math.sin(2 * math.pi * x / L3 + G3 + s['j3']))


# ---------------------------------------------------------------- stroke setup
def make_strokes():
    # peak half-widths, boldest first; colours are paired to weight so the heaviest
    # ribbons are teal/olive family and rust/tan sit at medium weight as accents.
    peaks = [30.0, 27.0, 25.0, 22.0, 20.0, 18.0, 15.0, 13.0, 12.0, 10.0, 9.0, 7.0, 6.0, 5.0, 4.0, 3.5, 3.0, 2.5]
    colors = [INK, DEEP, SLATE, OLIVE, TEAL, DOLIVE, RUST, TEAL, OLIVE, DEEP, RUST, TAN, TEAL, SLATE, OLIVE, TEAL, INK, DEEP]
    n = len(peaks)

    # lengths: two (near) full-width, a run of long/medium, a few short
    fracs = [1.0, 0.98, 0.92, 0.85, 0.78, 0.72, 0.66, 0.60, 0.56, 0.52, 0.50, 0.48, 0.45, 0.42, 0.40, 0.38, 0.36, 0.34]
    fracs = [min(1.0, f + random.uniform(-0.03, 0.03)) for f in fracs]
    random.shuffle(fracs)

    # vertical anchors: stratified across the band (guarantees spread + gaps), then shuffled
    anchors = [-46.0 + 92.0 * (i + random.uniform(0.15, 0.85)) / n for i in range(n)]
    random.shuffle(anchors)

    # start positions: stratified slots so short strokes are spread left-to-right
    slots = list(range(n))
    random.shuffle(slots)

    strokes = []
    for i in range(n):
        length = fracs[i] * W
        lo, hi = -30.0, W + 30.0 - length
        x0 = lo + (hi - lo) * (slots[i] + random.uniform(0.1, 0.9)) / n
        x1 = x0 + length
        # opposite-sign drift on alternating strokes -> neighbours cross each other
        drift = random.uniform(12, 40) * (1 if i % 2 == 0 else -1)
        strokes.append(dict(
            color=colors[i],
            peak=peaks[i],
            x0=x0, x1=x1,
            off0=anchors[i] - drift / 2.0,
            off1=anchors[i] + drift / 2.0,
            amp=random.uniform(0.85, 1.20),
            j1=random.uniform(-0.30, 0.30),
            j2=random.uniform(-0.70, 0.70),
            j3=random.uniform(0, 2 * math.pi),
            p=random.uniform(1.3, 2.2),                # taper sharpness
            q=random.uniform(0.80, 1.25),              # skews where the thickest point sits
            n1=random.uniform(0, 2 * math.pi), f1=random.uniform(1.5, 3.0),
            n2=random.uniform(0, 2 * math.pi), f2=random.uniform(3.5, 6.0),
            opacity=1.0,
            dry=None,
        ))

    # dry-brush tails: three medium-weight strokes break into dashes near their end
    candidates = [s for s in strokes if 9.0 <= s['peak'] <= 22.0]
    random.shuffle(candidates)
    for s in candidates[:3]:
        s['dry'] = dict(start=random.uniform(0.55, 0.70), count=random.randint(2, 3))

    # two of the thin strokes at 0.85 opacity
    thin = sorted(strokes, key=lambda s: s['peak'])[:4]
    random.shuffle(thin)
    for s in thin[:2]:
        s['opacity'] = 0.85

    return strokes


# ---------------------------------------------------------------- geometry
def center_y(s, x):
    t = (x - s['x0']) / (s['x1'] - s['x0'])
    return CENTER + s['off0'] + (s['off1'] - s['off0']) * t + swell(x, s)


def half_width(s, t):
    """peak * sin(t*pi)^p with gentle noise; t in [0,1] along the whole stroke."""
    tt = min(1.0, max(0.0, t)) ** s['q']
    env = max(0.0, math.sin(tt * math.pi)) ** s['p']
    noise = (1.0 + 0.12 * math.sin(2 * math.pi * s['f1'] * t + s['n1'])
             + 0.07 * math.sin(2 * math.pi * s['f2'] * t + s['n2']))
    return max(0.0, s['peak'] * env * noise)


def pieces_for(s):
    """(ta, tb, kind) spans in stroke-parameter space; kind: 'solid' | 'head' | 'dash'."""
    if not s['dry']:
        return [(0.0, 1.0, 'solid')]
    ts = s['dry']['start']
    out = [(0.0, ts, 'head')]                          # solid head that lifts off at ts
    t = ts
    remaining = 1.0 - ts
    count = s['dry']['count']
    weights = [1.0 / (k + 1.3) for k in range(count)]  # dashes shrink toward the tail
    total_w = sum(weights)
    for k in range(count):
        gap = remaining * random.uniform(0.06, 0.11)
        dash = remaining * 0.78 * weights[k] / total_w
        a = t + gap
        b = min(1.0, a + dash)
        if b - a > 0.02:
            out.append((a, b, 'dash'))
        t = b
    return out


def sample_piece(s, ta, tb, kind):
    span = s['x1'] - s['x0']
    xa, xb = s['x0'] + ta * span, s['x0'] + tb * span
    n = max(8, int((xb - xa) / STEP)) + 1
    pts = []
    for k in range(n):
        u = k / (n - 1)
        t = ta + (tb - ta) * u
        x = xa + (xb - xa) * u
        hw = half_width(s, t)
        if kind == 'head':
            hw *= min(1.0, (1.0 - u) / 0.30) ** 0.7   # lift-off at the end of the head
        elif kind == 'dash':
            hw *= math.sin(u * math.pi) ** 0.55       # lens-shaped dash
        pts.append([x, center_y(s, x), hw])
    return pts


def offset_pts(pts, frac, wfrac):
    """A thin sliver riding inside a stroke: offset along the normal by frac*hw, width wfrac*hw, tapered."""
    n = len(pts); res = []
    for k in range(n):
        x, y, hw = pts[k]
        xp, yp, _ = pts[max(0, k - 1)]; xn, yn, _ = pts[min(n - 1, k + 1)]
        tx, ty = xn - xp, yn - yp; ln = math.hypot(tx, ty) or 1.0
        nx, ny = -ty / ln, tx / ln
        u = k / (n - 1); taper = math.sin(u * math.pi) ** 0.6
        res.append([x + nx * hw * frac, y + ny * hw * frac, max(1.4, hw * wfrac) * taper])
    return res


def fmt(v):
    r = round(v, 1)
    return str(int(r)) if r == int(r) else str(r)


def ribbon_path(pts):
    """Offset the centerline by its half-width along the normal on both sides."""
    n = len(pts)
    top, bot = [], []
    for k in range(n):
        x, y, hw = pts[k]
        xp, yp, _ = pts[max(0, k - 1)]
        xn, yn, _ = pts[min(n - 1, k + 1)]
        tx, ty = xn - xp, yn - yp
        ln = math.hypot(tx, ty) or 1.0
        nx, ny = -ty / ln, tx / ln
        top.append((x + nx * hw, y + ny * hw))
        bot.append((x - nx * hw, y - ny * hw))
    d = ['M%s,%s' % (fmt(top[0][0]), fmt(top[0][1]))]
    for x, y in top[1:]:
        d.append('L%s,%s' % (fmt(x), fmt(y)))
    for x, y in reversed(bot):
        d.append('L%s,%s' % (fmt(x), fmt(y)))
    d.append('Z')
    return ''.join(d)


# ---------------------------------------------------------------- build
def build_svg():
    strokes = make_strokes()

    # sample everything first so the whole composition can be remapped into the band
    sampled = []
    for s in strokes:
        for (ta, tb, kind) in pieces_for(s):
            sampled.append((s, sample_piece(s, ta, tb, kind)))

    ymin = min(p[1] - p[2] for _, pts in sampled for p in pts)
    ymax = max(p[1] + p[2] for _, pts in sampled for p in pts)
    scale = (Y_BOT - Y_TOP) / (ymax - ymin)
    for _, pts in sampled:
        for p in pts:
            p[1] = Y_TOP + (p[1] - ymin) * scale

    # bold ribbons at the back, whiskers on top
    sampled.sort(key=lambda sp: -sp[0]['peak'])

    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
           'width="%d" height="%d" role="img" aria-label="Painted wave divider">'
           % (W, H, W, H)]
    for s, pts in sampled:
        op = '' if s['opacity'] >= 1.0 else ' fill-opacity="%s"' % fmt(s['opacity'])
        out.append('<path fill="%s"%s d="%s"/>' % (s['color'], op, ribbon_path(pts)))
    # cream slivers "cut" into the bold strokes, like a linocut
    CREAM = '#fff2ea'
    for s, pts in sampled:
        if s['peak'] < 12 or len(pts) < 20:
            continue
        for _ in range(random.choice([1, 1, 2])):
            frac = random.choice([-1, 1]) * random.uniform(0.25, 0.5)
            a = random.uniform(0.08, 0.35); b = min(0.95, a + random.uniform(0.3, 0.6))
            sub = [p for i, p in enumerate(pts) if a <= i / (len(pts) - 1) <= b]
            if len(sub) < 6:
                continue
            out.append('<path fill="%s" d="%s"/>' % (CREAM, ribbon_path(offset_pts(sub, frac, 0.16))))
    out.append('</svg>\n')
    return '\n'.join(out)


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('usage: %s OUTPUT.svg\n' % sys.argv[0])
        sys.exit(1)
    svg = build_svg()
    with open(sys.argv[1], 'w', encoding='utf-8') as fh:
        fh.write(svg)
    print('ok')


if __name__ == '__main__':
    main()
