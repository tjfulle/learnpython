import os
import shutil

D = os.path.dirname(os.path.realpath(__file__))
contents = os.listdir(D)
assert 'A Tale of Two Cities.txt' in contents

d = os.path.join(D, 'ThinkPython')
if os.path.isdir(d):
    shutil.rmtree(d)
contents.remove('figs')
shutil.copytree(os.path.join(D, 'figs'), os.path.join(d, 'figs'))

for item in contents:
    if os.path.isdir(item):
        continue
    if item == 'sanitize.py':
        continue
    src = os.path.join(D, os.path.basename(item))
    dst = os.path.join(d, os.path.basename(item))
    assert os.path.exists(src)
    shutil.copy(src, dst)
