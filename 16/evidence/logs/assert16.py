#!/usr/bin/env python3
"""Issue #16 P-2: extract compiled palettes from public/abridge.css, assert
SC-2 (mapped f1/c1/a1 both modes), SC-3 (direct-anchor fidelity), SC-4
(derived roles present), SC-5 (28 floored pairs >= 4.5:1)."""
import re, sys, json

css = open('public/abridge.css').read()

def block(pattern):
    m = re.search(pattern + r'\{([^}]*)\}', css)
    assert m, f'mode block not found: {pattern}'
    out = {}
    for prop in m.group(1).split(';'):
        if ':' in prop:
            k, _, v = prop.partition(':')
            out[k.strip().lstrip('-').strip()] = v.strip()
    return out

dark = block(r':root:not\(\.switch\)')
light = block(r':root\.switch')

# mapping tables of record (spec, 2026-10-26 extraction-derived cells resolved 2026-10-27)
DARK_EXPECT = {
    'cs': 'dark', 'f1': '#e1e7ec', 'f2': '#52b2a6', 'c1': '#1e2427', 'c2': '#1a2f30',
    'c3': '#00423c', 'c4': '#8a949b', 'a1': '#52b2a6', 'a2': '#6fd4c2', 'a3': '#2d93c5',
    'a4': '#8a949b', 'cg': '#13a092', 'cr': '#d97166',
}
LIGHT_EXPECT = {
    'cs': 'light', 'f1': '#545e69', 'f2': '#1e2427', 'c1': '#ffffff', 'c2': '#e1e7ec',
    'c3': '#ccd5db', 'c4': '#545e69', 'a1': '#006973', 'a2': '#007271', 'a3': '#265e88',
    'a4': '#00423c', 'cg': '#0f8176', 'cr': '#cd4335',
}

def norm(v):
    v = v.strip().lower()
    m = re.fullmatch(r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3', v)
    if m:  # #aabbcc stays
        return v
    m = re.fullmatch(r'#([0-9a-f])([0-9a-f])([0-9a-f])', v)
    if m:  # #abc -> #aabbcc
        return '#' + ''.join(c * 2 for c in m.groups())
    return v

print('--- SC-2: --f1/--c1/--a1 in both blocks ---')
for blk, expect, name in ((dark, DARK_EXPECT, 'dark'), (light, LIGHT_EXPECT, 'light')):
    for role in ('f1', 'c1', 'a1'):
        got, want = norm(blk[role]), norm(expect[role])
        ok = got == want
        print(f'  {"OK " if ok else "FAIL"} {name} --{role}: {got} (want {want})')

print('--- SC-3: direct-anchor fidelity (8 dark + 11 light color cells) ---')
DARK_DIRECT = {k: v for k, v in DARK_EXPECT.items() if k not in ('c2', 'a2', 'cg', 'cr')}
# dark direct cells: f1,f2,c1,c3,c4,a1,a3,a4 (cs is the mode flag; c2,a2,cg,cr derived)
DARK_DIRECT = {k: DARK_EXPECT[k] for k in ('f1', 'f2', 'c1', 'c3', 'c4', 'a1', 'a3', 'a4')}
LIGHT_DIRECT = {k: LIGHT_EXPECT[k] for k in ('f1', 'f2', 'c1', 'c2', 'c3', 'c4', 'a1', 'a3', 'a4', 'cg', 'cr')}
bad = 0
for role, want in DARK_DIRECT.items():
    got = norm(dark[role])
    ok = got == want; bad += not ok
    print(f'  {"OK " if ok else "FAIL"} dark --{role}: {got} (table {want})')
for role, want in LIGHT_DIRECT.items():
    got = norm(light[role])
    ok = got == want; bad += not ok
    print(f'  {"OK " if ok else "FAIL"} light --{role}: {got} (table {want})')
print(f'  direct-anchor mismatches: {bad}')

print('--- SC-4: derived roles present in compiled blocks ---')
for k in ('c2', 'a2', 'cg', 'cr'):
    print(f'  dark --{k}: {dark[k]}'); print(f'  light --{k}: {light[k]}')
for k in ('a2',):
    print(f'  light --{k}: {light[k]}')

# SC-5: R-3's 28 floored pairs, WCAG 2.1 relative luminance
def _chan(c8):
    c = c8 / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return 0.2126 * _chan(r) + 0.7152 * _chan(g) + 0.0722 * _chan(b)

def ratio(fg, bg):
    l1, l2 = sorted((lum(fg), lum(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

pairs = []
for role in ('f1', 'f2', 'a1', 'a2', 'a4'):
    for bg in ('c1', 'c2'):
        pairs.append((f'dark {role}/{bg}', dark[role], dark[bg]))
pairs.append(('dark a3/c1', dark['a3'], dark['c1']))
pairs.append(('dark mark c1d-text/c4d-bg', dark['c1'], dark['c4']))
pairs += [('dark cg/c1', dark['cg'], dark['c1']), ('dark cr/c1', dark['cr'], dark['c1'])]
for role in ('f1', 'f2', 'a1', 'a2', 'a4'):
    for bg in ('c1', 'c2'):
        pairs.append((f'light {role}/{bg}', light[role], light[bg]))
pairs.append(('light a3/c1', light['a3'], light['c1']))
pairs.append(('light mark c1-text/c4-bg', light['c1'], light['c4']))
pairs += [('light cg/c1', light['cg'], light['c1']), ('light cr/c1', light['cr'], light['c1'])]

print('--- SC-5: 28 floored pairs ---')
flo = 0
for name, fg, bg in pairs:
    fg, bg = norm(fg), norm(bg)
    r = ratio(fg, bg)
    flag = 'OK ' if r >= 4.5 else 'FAIL'
    flo += r < 4.5
    print(f'  {flag} {name:32s} {fg} on {bg}  {r:6.3f}:1')
print(f'  pairs={len(pairs)} failures={flo}')
print(f'\nRESULT: {"ALL GREEN" if bad == 0 and flo == 0 else "FAILURES PRESENT"}')
sys.exit(0 if (bad == 0 and flo == 0) else 1)