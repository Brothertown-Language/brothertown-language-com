#!/usr/bin/env python3
"""Compare two public/ trees: same file set? which files differ by content hash?"""
import os, hashlib, sys

def scan(root):
    out = {}
    for dp, _dn, fn in os.walk(root):
        for f in fn:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root)
            h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
            out[rel] = h
    return out

base = scan('/tmp/opencode/wt-base/public')
curr = scan('public')
print(f'files: base={len(base)} curr={len(curr)}')
only_base = sorted(set(base) - set(curr))
only_curr = sorted(set(curr) - set(base))
differ = sorted(k for k in set(base) & set(curr) if base[k] != curr[k])
print('paths only in base   :', only_base or 'NONE')
print('paths only in current:', only_curr or 'NONE')
print('content-diff paths   :')
for d in differ:
    print('  ', d)
print(f'\n{"SAME SET" if not (only_base or only_curr) else "SET DIFFERS"}, differing files: {len(differ)}')