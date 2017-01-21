import numpy as np


x=np.array([[3,6],[4,7],[2,6],[4,8]])
y=[9,11,8,12]

np.random.seed(2)

m,n=np.shape(x)
theta=np.random.rand(n)

print "Initial value of weights" 
print theta

h=np.dot(x.T,x)
theta=np.dot(np.linalg.inv(h),x.T)
theta=np.dot(theta,y)

print "Final value of weights"
print theta
print "Addition of 34 and 6 is equal to"
print np.dot(np.array([[34,6]]),theta)
