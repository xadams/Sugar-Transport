from numpy import empty,loadtxt
from matplotlib.pyplot import plot, fill_betweenx

def poreplot(dataset):

    data = loadtxt(dataset)
    N = len(data)
    x = empty([N], float)
    y = empty([N], float)
    x = data[:, 0]
    y = data[:, 1]
    plot(x, y,label=dataset)
    fill_betweenx(y, x)
