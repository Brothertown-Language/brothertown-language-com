#!/usr/bin/env python3
"""Issue #16 P-1: derive the five palette values, prove them against R-3's floor."""
import colorsys, itertools

# --- WCAG 2.1 SC 1.4.3 relative luminance (sRGB), per understanding page (2026-10-27 check) ---
def _chan(c8):
    c = c8 / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(h):
    h = h.lstrip('#')
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return 0.2126 * _chan(r) + 0.7152 * _chan(g) + 0.0722 * _chan(b)

def ratio(fg, bg):
    l1, l2 = sorted((lum(fg), lum(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

def mix_hex(a, b, t):
    """linear blend a->b by t in [0,1], rounded to hex"""
    aa = tuple(int(a.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    bb = tuple(int(b.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    v = tuple(round(x + (y - x) * t) for x, y in zip(aa, bb))
    return '#%02x%02x%02x' % v

def lighten_keep_hue(h, target_l):  # raise lightness in HSL until contrast target met, keep hue/sat
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16)/255 for i in (0, 2, 4))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    for step in range(0, 100001):
        trial = min(ll + step * 0.0005, 1.0)
        rr, gg, bb = colorsys.hls_to_rgb(hh, trial, ss)
        cand = '#%02x%02x%02x' % (round(rr*255), round(gg*255), round(bb*255))
        if lum(cand) >= target_l:
            return cand
    raise RuntimeError

# --- anchors (mapping tables of record; extraction 2026-10-26) ---
DARK = {'f1d': '#e1e7ec', 'f2d': '#52b2a6', 'c1d': '#1e2427', 'c3d': '#00423c',
        'c4d': '#8a949b', 'a1d': '#52b2a6', 'a3d': '#2d93c5', 'a4d': '#8a949b'}
LIGHT = {'f1': '#545e69', 'f2': '#1e2427', 'c1': '#ffffff', 'c2': '#e1e7ec',
         'c3': '#ccd5db', 'c4': '#545e69', 'a1': '#006973', 'a3': '#265e88',
         'a4': '#00423c', 'cg': '#0f8176', 'cr': '#cd4335'}

# --- derived 1: $c2d — charcoal-teal tint of $c1d toward logo teal #007a6f,
# brightest passing a4d (the binding darkest floored role on c2d) ---
l4 = lum('#8a949b')
cap_c2d = (l4 + 0.05) / 4.5 - 0.05
best_c2d = None
for i in range(1, 101):  # brightest passing tint
    t = i / 100.0
    cand = mix_hex('#1e2427', '#007a6f', t)
    if lum(cand) <= cap_c2d:
        best_c2d = (t, cand)
best_c2d_t, c2d = best_c2d

# --- derived 2: $a2d — aqua tint brighter than $a1d #52b2a6 (logo aqua cluster
# family, toward the bright #60c0a8 cluster rep), >=4.5 on c1d AND c2d with margin ---
def best_rising(base, toward, targets, floor_on_values, margin=0.10):
    for i in range(0, 101):
        t = i / 100.0
        cand = mix_hex(base, toward, t)
        rs = [ratio(cand, v) for v in floor_on_values]
        if all(r >= 4.5 + margin for r in rs):
            return t, cand
    raise RuntimeError

a2d_t, a2d = ('0.00 (kept) ', '#52b2a6')
for i in range(1, 101):
    t = i / 100.0
    cand = mix_hex('#52b2a6', '#6fd4c2', t)  # brightened aqua, same family/hue region
    if lum(cand) > lum('#52b2a6') and \
       ratio(cand, '#1e2427') >= 4.6 and ratio(cand, c2d) >= 4.6:
        a2d_t, a2d = t, cand

# --- derived 3: $cgd — favicon teal #0f8176 lightened, hue kept, >=4.5 on c1d ---
cgd = lighten_keep_hue('#0f8176', (lum('#1e2427') + 0.05) * 4.5 - 0.05 + 0.10/4.5*0)

# safer: explicit search with margin
def l_target(bg, margin=0.10):
    return (lum(bg) + 0.05) * 4.5 - 0.05 + margin / 4.5

cgd = lighten_keep_hue('#0f8176', l_target('#1e2427'))
crd = lighten_keep_hue('#cd4335', l_target('#1e2427'))

# --- derived 4 (light): $a2 — between wordmark teals #006973/#007a6f; brightest
# passing >=4.5 on #ffffff and #e1e7ec ---
best = None
for i in range(101):
    t = i / 100.0
    cand = mix_hex('#006973', '#007a6f', t)
    if ratio(cand, '#ffffff') >= 4.6 and ratio(cand, '#e1e7ec') >= 4.6:
        best = (t, cand)
if not best:
    # fall back: exact midpoint must pass at floor; else darker half toward #006973
    for i in range(51):
        t = 0.5 - i * 0.01
        cand = mix_hex('#006973', '#007a6f', t)
        if ratio(cand, '#ffffff') >= 4.5 and ratio(cand, '#e1e7ec') >= 4.5:
            best = (t, cand); break
a2_t, a2 = best

print('=== derived values ===')
print(f'c2d: {c2d}  (blend t={best_c2d_t} toward #007a6f; L={lum(c2d):.4f} cap={cap_c2d:.4f})')
print(f'a2d: {a2d}  (blend t={a2d_t} of #52b2a6 -> bright aqua; L={lum(a2d):.4f})')
print(f'cgd: {cgd}  (lightened from #0f8176, hue kept; L={lum(cgd):.4f} need>={l_target("#1e2427"):.4f})')
print(f'crd: {crd}  (lightened from #cd4335, hue kept; L={lum(crd):.4f} need>={l_target("#1e2427"):.4f})')
print(f'a2 : {a2}  (blend t={a2_t} between #006973/#007a6f; L={lum(a2):.4f})')

print('\n=== 28 floored pairs (R-3) ===')
dark = dict(DARK, c2d=c2d, a2d=a2d, cgd=cgd, crd=crd)
light = dict(LIGHT, a2=a2)
pairs = []
for role in ('f1d', 'f2d', 'a1d', 'a2d', 'a4d'):
    for bg in ('c1d', 'c2d'):
        pairs.append((role, bg, dark[role], dark[bg]))
pairs += [('a3d', 'c1d', dark['a3d'], dark['c1d'])]
pairs += [('mark-dark (c1d text on c4d)', 'c4d', dark['c1d'], dark['c4d'])]
pairs += [('cgd', 'c1d', dark['cgd'], dark['c1d']), ('crd', 'c1d', dark['crd'], dark['c1d'])]
for role in ('f1', 'f2', 'a1', 'a2', 'a4'):
    for bg in ('c1', 'c2'):
        pairs.append((role, bg, light[role], light[bg]))
pairs += [('a3', 'c1', light['a3'], light['c1'])]
pairs += [('mark-light (c1 text on c4)', 'c4', light['c1'], light['c4'])]
pairs += [('cg', 'c1', light['cg'], light['c1']), ('cr', 'c1', light['cr'], light['c1'])]

fails = 0
for name, bgrole, fg, bg in pairs:
    r = ratio(fg, bg)
    flag = 'OK ' if r >= 4.5 else 'FAIL'
    if r < 4.5: fails += 1
    print(f'{flag} {name:26s} {fg} on {bg}  {r:5.2f}:1')
print(f'\nTOTAL: {len(pairs)} pairs, failures={fails}')
assert fails == 0, 'R-3 floor violated'