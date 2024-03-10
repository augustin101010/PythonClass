import matplotlib.pyplot as plt
import numpy as np

# import matplotlib
# 
# plt.rcParams['figure.figsize'] = [10, 10]
# font = {'weight' : 'bold',
#         'size'   : 18}
# matplotlib.rc('font', **font)

def plot_line(start,end,color="blue",label="",npoints=1000):
    x_axis = [ start[0]+(end[0]-start[0])*i/npoints for i in range(npoints) ]
    y_axis = [ start[1]+(end[1]-start[1])*i/npoints for i in range(npoints) ]
    if label != "":
        plt.plot(x_axis,y_axis,color=color,label=label)
    else:
        plt.plot(x_axis,y_axis,color=color)

a = np.array([1,2])
b = np.array([0,4])
c = np.array([-1,3])

centroid = np.array([-1/(3+np.sqrt(3)),1/6 *(21 - np.sqrt(3))])

plot_line(a,b,color="green",label="a")
plot_line(b,c,color="purple",label="b")
plot_line(c,a,color="orange",label="c")

plot_line(a,centroid,color="yellow",label="x")
plot_line(b,centroid,color="blue",label="y")
plot_line(c,centroid,color="red",label="z")
plt.legend()
plt.savefig("Triangle.png")