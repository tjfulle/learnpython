import numpy as np

a = np.loadtxt('data.txt', delimiter=',', skiprows=1)
a = a[:, [2,3]]
a.sort(axis=1)

b = []
fn = lambda x: np.interp(x, a[:,0], a[:,1])
b = np.array([[x, fn(x)*10] for x in np.linspace(0, .15)])

fh = open('data.csv', 'w')
fh.write('Strain, Stress\n')
np.savetxt(fh, b, delimiter=',')
