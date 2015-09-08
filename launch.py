#!/usr/bin/env python
import os
import sys
import signal
from subprocess import Popen
from argparse import ArgumentParser
from os.path import dirname, realpath, join

D = dirname(realpath(__file__))
IPY_D = join(D, 'Python-2.7')

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    p = ArgumentParser()
    args, other = p.parse_known_args(argv)
    a = other
    env = dict(os.environ)
    env['JUPYTER_CONFIG_DIR'] = IPY_D
    env['IPYTHONDIR'] = IPY_D
    command = 'ipython notebook Introduction.ipynb'
    try:
        proc = Popen(command, env=env, shell=True, preexec_fn=os.setsid)
    except KeyboardInterrupt:
        os.killpg(proc.pid, signal.SIGTERM)
    return 0

if __name__ == '__main__':
    main()
