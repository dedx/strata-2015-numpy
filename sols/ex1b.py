#method 1
b = np.diag(np.arange(1.,7.))
b = b[:,1:]
print b
print

#method 2
v = np.array(np.zeros(5.))
h = np.array(np.diag([2.,3.,4.,5.,6.]))
c = np.vstack((v,h))
print c
