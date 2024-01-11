import matplotlib.pyplot as plt
import numpy as np 

X=[1,2,3,4,5]
x=3

Y=np.array([3,5,7,8,10])
y=np.mean(Y)


print(f"Data X={X},mean of x={x},Data Y={Y},mean of y={y}")
SSxx=0
SSyy=0

for i in X : # i will print elements of x not index 
  SSxx += ((i-x)**2)
  
for i in Y : # i will print elements of x not index 
  SSyy += ((i-y)**2)

print(SSxx)
print (SSyy)





'''
plt.scatter(X, Y, label="Data points")
plt.plot(X, [m * x + b for x in X], color='red',label="Best fitting")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)

plt.show()
'''