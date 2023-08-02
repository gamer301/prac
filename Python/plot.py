import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.scatter(xpoints, ypoints,marker='+',ms-25,mc='b',label='random') 
# u can just use x or y point and it wil take default value from 1,2,3,4 with step of 1 
#plt.plot(xpoints,marker='H') if u dont use market argument the point won't be connected and only specific points will be marked withou joining them with line 

plt.show()