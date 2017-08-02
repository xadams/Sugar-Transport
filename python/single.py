from matplotlib.pylab import plot, show, xlabel, ylabel, xlim, ylim, title, fill_betweenx, legend
from poreplot import poreplot
import sys
import matplotlib.pyplot

def save_figure(name):
    # change these if wanted
    do_save = True
    fig_dir = './'
    if do_save:
        matplotlib.pyplot.savefig(fig_dir + name, bbox_inches='tight')

# load in the attached txt file (which should have 2 columns of data corresponding to the z position and pore radius
name = sys.argv[1]

# call the poreplot function from the included python file
poreplot(name)

# saves the resulting plot 
xlabel("Pore Radius (Å)",fontsize=18)
ylabel("Distance along transport path (Å)",fontsize=18)
xlim(0.5,4.0)
title(name,fontsize=24)
save_figure("tmp.png")
