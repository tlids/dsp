# Matrix Algebra

import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])

u = np.matrix([6,2,-3,5])
v = np.matrix([3,5,-1,4])
w = np.matrix([1,8,0,5]).transpose()

# 1.1
print (np.shape(A))

# 1.2
print (np.shape(B))

# 1.3
print (np.shape(C))

# 1.4
print (np.shape(D))

# 1.5
print (np.shape(u))

# 1.6
print (np.shape(w))

# 2.1
u + v

# 2.2
u - v

# 2.3
a = 6
a*u

# 2.4
int(u*(v.transpose()))

# 2.5
np.linalg.norm(u)

# 3.1
print ('not defined')

# 3.2
print ('defined')
A - C.transpose()

# 3.3
print ('defined')
C.transpose() + 3 * D

# 3.4
print ('defined')
B * A

# 3.5
print ('not defined')
