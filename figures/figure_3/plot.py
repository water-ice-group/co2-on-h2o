import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


#######################################################################
######################## LOAD THE DATA ################################
#######################################################################

''' Outputs v1 and v2 stem from the two interfaces present in our 
simulation box. '''

dat_BLYP = dict()
counter = 1
step = 1
# ---------------------------------------------------------------------
dir = './BLYP-D3/low_pressures/'
for i in range(0,6):
    x = np.loadtxt(dir + str(i) + '/outputs_v1/C_dens.dat')[::step,0]
    x = [i+0.1 for i in x]
    y_1 = np.loadtxt(dir + str(i) + '/outputs_v1/C_dens.dat')[::step,1]
    y_2 = np.loadtxt(dir + str(i) + '/outputs_v2/C_dens.dat')[::step,1]
    output = [(y_1[i] + y_2[i])/2 for i in range(len(y_1))]
    dat_BLYP[counter] = np.array([x, output]).T
    counter += 1
dir = './BLYP-D3/intermediate_pressures/'
for i in range(0,6):
    x = np.loadtxt(dir + str(i) + '/outputs_v1/C_dens.dat')[::step,0]
    x = [i+0.1 for i in x]
    y_1 = np.loadtxt(dir + str(i) + '/outputs_v1/C_dens.dat')[::step,1]
    y_2 = np.loadtxt(dir + str(i) + '/outputs_v2/C_dens.dat')[::step,1]
    output = [(y_1[i] + y_2[i])/2 for i in range(len(y_1))]
    dat_BLYP[counter] = np.array([x, output]).T
    counter += 1
dir = './BLYP-D3/high_pressures/'
for i in range(1,6):
    x = np.loadtxt(dir + str(i) + '/outputs_v1/C_dens.dat')[::step,0]
    x = [i+0.1 for i in x]
    y_1 = np.loadtxt(dir + str(i) + '/outputs_v1/C_dens.dat')[::step,1]
    y_2 = np.loadtxt(dir + str(i) + '/outputs_v2/C_dens.dat')[::step,1]
    output = [(y_1[i] + y_2[i])/2 for i in range(len(y_1))]
    dat_BLYP[counter] = np.array([x, output]).T
    counter += 1
# ---------------------------------------------------------------------


# Density - Water
dat_BLYP_water = dict()
counter = 1
step = 1
# ---------------------------------------------------------------------
dir = './BLYP-D3/low_pressures/'
for i in range(0,6):
    x = np.loadtxt(dir + str(i) + '/outputs_v1/OW_dens.dat')[::step,0]
    x = [i+0.1 for i in x]
    y_1 = np.loadtxt(dir + str(i) + '/outputs_v1/OW_dens.dat')[::step,1]
    y_2 = np.loadtxt(dir + str(i) + '/outputs_v2/OW_dens.dat')[::step,1]
    output = [(y_1[i] + y_2[i])/2 for i in range(len(y_1))]
    dat_BLYP_water[counter] = np.array([x, output]).T
    counter += 1
dir = './BLYP-D3/intermediate_pressures/'
for i in range(0,6):
    x = np.loadtxt(dir + str(i) + '/outputs_v1/OW_dens.dat')[::step,0]
    x = [i+0.1 for i in x]
    y_1 = np.loadtxt(dir + str(i) + '/outputs_v1/OW_dens.dat')[::step,1]
    y_2 = np.loadtxt(dir + str(i) + '/outputs_v2/OW_dens.dat')[::step,1]
    output = [(y_1[i] + y_2[i])/2 for i in range(len(y_1))]
    dat_BLYP_water[counter] = np.array([x, output]).T
    counter += 1
dir = './BLYP-D3/high_pressures/'
for i in range(1,6):
    x = np.loadtxt(dir + str(i) + '/outputs_v1/OW_dens.dat')[::step,0]
    x = [i+0.1 for i in x]
    y_1 = np.loadtxt(dir + str(i) + '/outputs_v1/OW_dens.dat')[::step,1]
    y_2 = np.loadtxt(dir + str(i) + '/outputs_v2/OW_dens.dat')[::step,1]
    output = [(y_1[i] + y_2[i])/2 for i in range(len(y_1))]
    dat_BLYP_water[counter] = np.array([x, output]).T
    counter += 1
# ---------------------------------------------------------------------

pressures = [1, 5, 10, 20, 30, 40, 60, 65, 70, 75, 80, 85, 100, 200, 300, 400, 500]



#######################################################################
############################ PLOT #####################################
#######################################################################


fig, ax = plt.subplots(figsize=(6,6))
plt.rcParams["font.family"] = "Arial"

# ---------------------------------------------------------------------
no_files = 18
def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)
# ---------------------------------------------------------------------


# plot of the water density
# ---------------------------------------------------------------------
c1='salmon'
c2='maroon'
n = no_files - 1
step = 1
for i in range(1, 18):
    ax.plot(dat_BLYP_water[i][::step, 0], dat_BLYP_water[i][::step, 1], '--',
        color=colorFader(c1, c2, i/n),alpha=( 0.5 + 0.5*(i/18)),
        label=pressures[i-1],
        linewidth=1.2)
    
ax.annotate(xy=(-3.2,0.78),text='1',size=10,color='salmon')
ax.annotate(xy=(-3.7,1.2),text='500',size=10,color='maroon')
# ---------------------------------------------------------------------


# plot of the CO2 density 
# ---------------------------------------------------------------------
c1='cyan'
c2='blue'
for i in range(1, 18):
    ax.plot(dat_BLYP[i][::step, 0], dat_BLYP[i][::step, 1], '-.',
            color=colorFader(c1, c2, i/n),linewidth=1.2)
    if i == 1:
        ax.annotate(xy=(dat_BLYP[i][-1, 0], dat_BLYP[i][-1, 1]), xytext=(5,0),
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    elif i == 2:
        ax.annotate(xy=(dat_BLYP[i-1][-1, 0], dat_BLYP[i-1][-1, 1]), xytext=(13,0),
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    elif i == 3:
        ax.annotate(xy=(dat_BLYP[i-2][-1, 0], dat_BLYP[i-2][-1, 1]), xytext=(21, 0),
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    elif i == 8:
        pass
    elif i == 9:
        pass
    elif i == 10:
        pass
    elif i == 11:
        pass
    elif i == 12:
        pass
    elif i == 13:
        ax.annotate(xy=(dat_BLYP[i][-1, 0], dat_BLYP[i][-1, 1]), xytext=(5, 0),
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    elif i == 14:
        ax.annotate(xy=(dat_BLYP[i][-1, 0], dat_BLYP[i][-1, 1]), xytext=(5, 0), 
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    elif i == 15:
        ax.annotate(xy=(dat_BLYP[i][-1, 0], dat_BLYP[i][-1, 1]), xytext=(5, -2),
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    elif i == 16:
        ax.annotate(xy=(dat_BLYP[i][-1, 0], dat_BLYP[i][-1, 1]), xytext=(5, 2),
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    elif i == 17:
        ax.annotate(xy=(dat_BLYP[i][-1, 0], dat_BLYP[i][-1, 1]), xytext=(5, 6), 
                    textcoords='offset points', text=pressures[i-1], va='center',
                    size=9, color=colorFader(c1, c2, i/n))
    else:
        ax.annotate(xy=(dat_BLYP[i][-1, 0], dat_BLYP[i][-1, 1]), xytext=(5, 0),
                textcoords='offset points', text=pressures[i-1], va='center',
                size=9, color=colorFader(c1, c2, i/n))
# ---------------------------------------------------------------------

# plot appearance
# ---------------------------------------------------------------------
ax.set_ylabel('Density  (g/ml)', size=14)
ax.set_xlabel(r'Distance  $(\mathrm{\AA})$', size=14)
ax.tick_params(axis="x", which='major', direction="in", labelsize=12,size=5,width=1)
ax.tick_params(axis="y", which='major', direction="in", labelsize=12,size=5,width=1)
ax.tick_params(axis="x", which='minor', direction="in", labelsize=12)
ax.tick_params(axis="y", which='minor', direction="in", labelsize=12)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.set_xlim(-10, 10)
ax.set_ylim(0,1.9)
# ---------------------------------------------------------------------
handles, labels = ax.get_legend_handles_labels()
ax.grid(ls='--')

plt.subplots_adjust(hspace=0.05)
plt.show()