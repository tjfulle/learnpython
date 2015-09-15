#!/usr/bin/env python
import os
import re
import sys
import signal
import subprocess
filename = sys.argv[1]
root, ext = os.path.splitext(filename)
lines = open(root + '.ipynb').read()
regex = re.compile(r'<a.*?>.*?<\/a>')
lines = regex.sub('', lines)
slides = root + '_slides.ipynb'
with open(slides, 'w') as fh:
    fh.write(lines)
reveal = '--reveal-prefix "http://cdn.jsdelivr.net/reveal.js/2.6.2"'
cmd = 'ipython nbconvert --to slides --post serve {0} {1}'.format(reveal, slides)
env = dict(os.environ)
D = os.path.dirname(os.path.realpath(__file__))
IPY_D = os.path.join(D, '../Python-2.7')
assert os.path.isdir(IPY_D)
env['JUPYTER_CONFIG_DIR'] = IPY_D
env['IPYTHONDIR'] = IPY_D
kwds = {'env': env}
try:
    kwds['preexec_fn'] = os.setsid
except AttributeError:
    pass
try:
    proc = subprocess.Popen(cmd.split(), **kwds)
    proc.wait()
except KeyboardInterrupt:
    os.killpg(proc.pid, signal.SIGTERM)

raise SystemExit('done')
