#!/usr/bin/env python
import os
import sys
import signal
from subprocess import Popen
from argparse import ArgumentParser
from os.path import dirname, realpath, join

D = dirname(realpath(__file__))
IPY_D = join(D, 'Python-2.7')

env = dict(os.environ)
env['JUPYTER_CONFIG_DIR'] = IPY_D
env['IPYTHONDIR'] = IPY_D
command = 'ipython notebook Introduction.ipynb'
kwds = {'env': env, 'shell': True}
try:
    kwds['preexec_fn'] = os.setsid
except AttributeError:
    pass
try:
    proc = Popen(command, **kwds)
    proc.wait()
except KeyboardInterrupt:
    os.killpg(proc.pid, signal.SIGTERM)
