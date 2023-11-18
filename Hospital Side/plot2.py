import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('dark_background')
#x,y=np.loadtxt('file.txt',delimiter='.',unpack=True)
x=np.loadtxt('tempu.txt',delimiter='\n',unpack=True)
#plt.plot(x,y,label='loaded from file')
plt.plot(x,label='heart rate')
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("heart rate graph")
plt.legend()
plt.grid(True)
plt.savefig("plot.png")

plt.show()

