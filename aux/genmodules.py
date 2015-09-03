import os
import shutil
D = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(D, '../')

def touch_init(d):
    with open(os.path.join(d, '__init__.py'), 'w') as fh:
        fh.write('\n')

def gen_module_examples():
    d0 = os.path.join(directory, 'image')
    if os.path.isdir(d0):
        shutil.rmtree(d0)
    os.makedirs(d0)
    touch_init(d0)

    d1 = os.path.join(d0, 'filetypes')
    os.makedirs(d1)
    touch_init(d1)
    for f in ('jpg.py', 'pdf.py', 'png.py'):
        with open(os.path.join(d1, f), 'w') as fh:
            fh.write("""
def open_image(filename):
    print 'opening {0}'.format(filename)""")

    d2 = os.path.join(d0, 'manipulate')
    os.makedirs(d2)
    touch_init(d2)
    for f in ('convert.py', 'crop.py', 'filter.py'):
        fun = f.split('.')[0]
        with open(os.path.join(d2, f), 'w') as fh:
            fh.write("""
def {0}(filename):
    print '{0}ing {{0}}'.format(filename)""".format(fun))
