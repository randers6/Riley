import numpy as np
import random 

X = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,],[1,2,2,2,3,3,4,5,5,5,6,6]])


Y = np.array([1,1.5,2,3,2,3,4,3,3.5,5,4.5,5])

a = np.random.random(1)[0]
b = np.random.random(1)[0]

theta=np.array([a,b])
thetatran=np.transpose(theta)


alpha = .001
grad = np.array([1.0,1.0])
toll =.01
Sum = 0
runs=0

while np.absolute(grad).max()> toll and runs<1000:
    runs=runs+1
    for ii in range(len(theta)):
        for mm in range(len(Y)): 
            Sum = Sum+X[ii,mm]*(Y[mm] - (np.dot(thetatran,X[:,mm]))) 
        grad[ii] = Sum
        theta[ii] = theta[ii]+alpha*Sum
       

print(theta)

  




        

  