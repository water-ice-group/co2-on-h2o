import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
import pandas as pd

#######################################################################
######################## LOAD THE DATA ################################
#######################################################################

# load model data
fin = np.loadtxt('./blyp-d3/data_3')
press_blyp = fin[:,0]
ift_blyp = fin[:,1]
err_blyp = fin[:,2]
press_blyp = [i*1.01325 for i in press_blyp] # convert from atmospheres to bar


# load experimental data
def load_exp_dat(loc):
    df_aimd = pd.read_csv(str(loc),header=None)
    x = df_aimd[0].tolist()
    y = df_aimd[1].tolist()
    return (x,y)

hinton = load_exp_dat('./experiment/hinton.csv')
bachu = load_exp_dat('./experiment/bachu.csv')
chun = load_exp_dat('./experiment/chun.csv')
hebach = load_exp_dat('./experiment/hebach.csv')
tewes = load_exp_dat('./experiment/tewes.csv')
georgiadis = load_exp_dat('./experiment/georgiadis.csv')



# load computational literature data
upper_x,upper_y = load_exp_dat('./comp/comp_upper.csv')
upper_x = [i*10 for i in upper_x]

lower_x,lower_y = load_exp_dat('./comp/comp_lower.csv')
lower_x = [i*10 for i in lower_x]


#######################################################################
############################ PLOT #####################################
#######################################################################


fig,ax=plt.subplots(figsize=(7,5))
ax.fill_between(lower_x,lower_y,upper_y,color='red',alpha=0.03)

# experimental data
ax.scatter(georgiadis[0],georgiadis[1],marker='p',facecolors='none',edgecolors='gray',
          label='Georgiadias et al. (297.9 K)')
ax.scatter(bachu[0],bachu[1],marker='x',color='orange',
          label='Bachu et al. (298.15 K)')
ax.scatter(chun[0],chun[1],marker='^',facecolors='none',edgecolors='violet',
          label='Chun et al. (298.15 K)')
ax.scatter(hebach[0],hebach[1],marker='s',facecolors='none',edgecolors='purple',
          label='Hebach et al. (298.3 K)')
ax.scatter(tewes[0],tewes[1],facecolors='none',edgecolors='lightblue',
          label='Tewes et al. (293.0 K)')
ax.scatter(hinton[0],hinton[1],marker='h',facecolors='none',edgecolors='black',
          label='Hinton et al. (295.5 K)')

# computational data
ax.plot(lower_x,lower_y, '--',color='red',label='Shiga et al. (313.0 K)',linewidth=0.8)
ax.plot(upper_x,upper_y, '--',color='red',linewidth=0.8)

# NNP data
ax.errorbar(press_blyp,ift_blyp,
            yerr=err_blyp,
            ecolor='b',
            capsize=5,
            linestyle='',
            marker='o',
            label='This work (300.0 K)',
            color='b')


ax.set_ylabel('IFT  (mN/m)',size=14)
ax.set_xlabel('Pressure  (bar)',size=14)

ax.spines[['top', 'right','bottom','left']].set_linewidth(1.0)

ax.tick_params(top=True, labeltop=False, bottom=True, labelbottom=True,which='both')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis='both',which='major',direction='in',labelsize=12,size=4.5)
ax.tick_params(axis='both',which='minor',direction='in',labelsize=12,size=3)

ax.set_yticks(np.arange(00,85,10))
ax.set_xticks(np.arange(00,510,50))
ax.set_xlim(-10,520)
ax.set_ylim(10,85)
ax.legend()
ax.grid(ls='--',alpha=0.5)
plt.show()
