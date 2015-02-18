#method 1
start = np.array([[4,3],[2,1]])
print np.tile(start,(2,3))
print

#method 2
c = np.array(np.tile((4,3),3))
d = np.array(np.tile((2,1),3))
e = np.array([c,d,c,d])
print e
