import numpy as np
import random 
import matplotlib.pyplot as ply

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
X = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,],x])


Y = np.array([1,2,4,4,5,6,7,8,9,9,11,12])

a=0
b=.9


theta=np.array([a,b])
thetatran=np.transpose(theta)


alpha = .001
grad = np.array([1.0,1.0])
toll =.0001
runs=0

while np.absolute(grad).max()> toll and runs<1000000:
    runs=runs+1
    for ii in range(len(theta)):
        Sum = 0
        for mm in range(len(Y)): 
            Sum = Sum+X[ii,mm]*(Y[mm] - (np.dot(thetatran,X[:,mm]))) 
        grad[ii] = Sum
        theta[ii] = theta[ii]+alpha*Sum
       

print(theta)
print(grad)
  

ply.scatter(x,Y)


xspan=np.linspace(0,12,num=100)
y=theta[0]+theta[1]*xspan
ply.plot(xspan,y)

ply.show()

       

  