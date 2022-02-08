#!/usr/bin/env python
import os
import signal
from subprocess import Popen
from os.path import dirname, realpath, join

D = dirname(realpath(__file__))
env = dict(os.environ)
command = 'jupyter lab'
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
