import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


#######################################################################
######################## LOAD THE DATA ################################
#######################################################################

''' Outputs v1 and v2 stem from the two interfaces present in our 
simulation box. '''

dat_BLYP = dict()
counter = 1
dir = './BLYP-D3/low_pressures/'
for i in range(0,6):
    x_range = np.loadtxt(dir + str(i) + '/outputs_v1/surf_co2_CO_angle_2.5.dat')[:,0]
    ang_1 = np.loadtxt(dir + str(i) + '/outputs_v1/surf_co2_CO_angle_2.5.dat')[:,1]
    ang_2 = np.loadtxt(dir + str(i) + '/outputs_v2/surf_co2_CO_angle_2.5.dat')[:,1]
    tot = [(ang_1[i] + ang_2[i])/2 for i in range(len(ang_2))]
    dat_BLYP[counter] = [x_range, tot]
    counter += 1
dir = './BLYP-D3/intermediate_pressures/'
for i in range(0,6):
    x_range = np.loadtxt(dir + str(i) + '/outputs_v1/surf_co2_CO_angle_2.5.dat')[:,0]
    ang_1 = np.loadtxt(dir + str(i) + '/outputs_v1/surf_co2_CO_angle_2.5.dat')[:,1]
    ang_2 = np.loadtxt(dir + str(i) + '/outputs_v2/surf_co2_CO_angle_2.5.dat')[:,1]
    tot = [(ang_1[i] + ang_2[i])/2 for i in range(len(ang_2))]
    dat_BLYP[counter] = [x_range, tot]
    counter += 1
dir = './BLYP-D3/high_pressures/'
for i in range(0,6):
    x_range = np.loadtxt(dir + str(i) + '/outputs_v1/surf_co2_CO_angle_2.5.dat')[:,0]
    ang_1 = np.loadtxt(dir + str(i) + '/outputs_v1/surf_co2_CO_angle_2.5.dat')[:,1]
    ang_2 = np.loadtxt(dir + str(i) + '/outputs_v2/surf_co2_CO_angle_2.5.dat')[:,1]
    tot = [(ang_1[i] + ang_2[i])/2 for i in range(len(ang_2))]
    dat_BLYP[counter] = [x_range, tot]
    counter += 1

avg_out = []
err_out = []
for i in range(len(dat_BLYP[1][0])):
    out = []
    for j in range(1,18):
        out.append(np.mean(dat_BLYP[j][1][i]))
    avg_out.append(np.average(out))
    err_out.append(np.std(out))

pressures = [1, 5, 10, 20, 30, 40, 60, 65, 70, 75, 80, 85, 85, 100, 200, 300, 400, 500]


#######################################################################
############################ PLOT #####################################
#######################################################################

import seaborn as sns
sns.set_palette("tab20c",8)
no_files = 19
def colorFader(c1,c2,mix=0): 
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)
c1='purple'
c2='tab:green'
n = no_files - 1

fig,ax = plt.subplots()
step = 5
for i in range(1,19):
    if i in [1,2,3,4,5,6,8,15]:
        ax.plot(dat_BLYP[i][0], dat_BLYP[i][1], label=str(pressures[i-1]) + ' bar')
        

ax.set_xlabel('Angle  (degrees)',size=12)
ax.set_ylabel('Distribution',size=12)
ax.tick_params(axis="x", which='both', direction="in", labelsize=12)
ax.tick_params(axis="y", which='both', direction="in", labelsize=12)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.grid(ls='--')
ax.legend(loc='upper right')
plt.show()