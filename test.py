import matplotlib.pyplot as plt
import numpy as np

c= 3*10**8

time, redshift1, redshift2 = np.loadtxt('Binary_data.csv', delimiter = ',', unpack = True)\


plt.figure(figsize=(15,3))
plt.plot(time,c*redshift1, 'b')
plt.plot(time,c*redshift2, 'r')
a=set(c*redshift1)
b=set(c*redshift2)

intersection_pts = a.intersection(b)
print("Points of intersection(y values only):",intersection_pts)
toList = list(intersection_pts)
print("\nAvg y val:",np.average(toList))
plt.xlabel('Time(y)')
plt.ylabel('radial velocity') # Normalized Strain is not strain\
plt.grid()
plt.show()
