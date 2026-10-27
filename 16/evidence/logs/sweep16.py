#!/usr/bin/env python3
"""Issue #16 P-3: SC-8 no-logo-duplication sweep.
(a) hash-compare tracked tree + public/** against the BI logo assets of record
(b) grep tracked tree + public/** for brothertownindians.org URLs
(c) dimension/aspect scan of public/** raster images for the logo (800x200,
    and any resized copy of its 4:1 aspect pair) and the favicon 180x180 mark.
"""
import os, hashlib, subprocess, sys
sys.path.insert(0, '/tmp/opencode/bi-colors/pylib')
from PIL import Image

ROOT = '/home/muksihs/git/brothertown-language-com'
targets = {
    '/tmp/opencode/bi-colors/BIN_logo_tagline800.png': '8120e2...',
    '/tmp/opencode/bi-colors/Tribe_Icon_favicon_180.png': '0a9f5...',
}
import math
logo_hashes = {}
for path in targets:
    with open(path, 'rb') as f:
        logo_hashes[os.path.basename(path)] = hashlib.sha256(f.read()).hexdigest()
print('assets of record hashes:')
for k, v in logo_hashes.items():
    print(f'  {k}: {v}')

hits_hash, hits_url, dims = [], [], []
# files: tracked tree + public/**
tracked = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, text=True).stdout.split('\0')
tracked = [t for t in tracked if t]
built = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.join(ROOT, 'public')) for f in fn]
paths = [os.path.join(ROOT, t) for t in tracked] + built

img_exts = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.ico'}
for p in paths:
    if not os.path.isfile(p):
        continue
    rel = os.path.relpath(p, ROOT)
    with open(p, 'rb') as f:
        data = f.read()
    if hashlib.sha256(data).hexdigest() in logo_hashes.values():
        hits_hash.append(rel)
    try:
        text = data.decode('utf-8', errors='strict')
    except UnicodeDecodeError:
        text = data.decode('latin-1', errors='ignore')
    if 'brothertownindians.org' in text:
        hits_url.append(rel)
    ext = os.path.splitext(p)[1].lower()
    if ext in img_exts:
        try:
            with Image.open(p) as im:
                w, h = im.size
                dims.append((rel, w, h))
        except Exception:
            pass

print('\n(a) hash comparisons vs assets of record:')
print('    hits:', hits_hash or 'NONE')
print('(b) brothertownindians.org references:')
print('    hits:', hits_url or 'NONE')

# (c) dimension scan: logo aspect 800x200 (0.25 ratio) or 800/600/200-width resizes with 0.25 ratio;
# favicon mark: 180x180 exact or 1:1 images whose size matches the known icon variants
logo_aspect_hits = [d for d in dims if abs((d[1] / d[2]) - 4.0) < 0.01]
favicon_hits = [d for d in dims if d[1] == d[2] == 180]
print('(c) public/** image dimension overview (logo-aspect + 180x180 candidates):')
print('    4:1-aspect images:', [d for d in logo_aspect_hits if '/public/' in d[0]] or 'NONE')
print('    180x180 images  :', [d for d in favicon_hits if '/public/' in d[0]] or 'NONE')
print('    all site-owned 1:1 images:', [f'{r} {w}x{h}' for r, w, h in dims if w == h and '/public/' in r])
print("\n    (site favicon family is the site's own branding — untouched by this change; listed for inspection)")
fails = bool(hits_hash) or bool(hits_url)
print(f'\nSC-8 RESULT: {"FAIL — remediate" if fails else "PASS — no copies, no hotlinks"}')
sys.exit(1 if fails else 0)