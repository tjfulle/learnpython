#!/usr/bin/env python
import os
import re
import sys
import signal
import subprocess
D = os.path.dirname(os.path.realpath(__file__))
filename = sys.argv[1]
root, ext = os.path.splitext(filename)
lines = open(root + '.ipynb').read()
regex = re.compile(r'<a.*?>.*?<\/a>')
lines = regex.sub('', lines)
slides = root + '_slides.ipynb'
with open(slides, 'w') as fh:
    fh.write(lines)
