"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
# LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# EXTERNAL FUNCTIONS
from lspm_apl import lspm_apl
from lspm import lspm
from roblspm import roblspm
from vaf import vaf
from dv2dm import dv2dm

# CODE
# READING DATA

U = pd.read_csv('data/retail/U_new.csv',header = None).to_numpy()
Y = pd.read_csv('data/retail/Y.csv',header = None).to_numpy()

# shortening Y columns (only first two remain)
# REWRITING NEEDED
Y = np.delete(Y,[2,3,4],axis=1)
# multiply first 10 elements in first column by 50
a = 10
Y[0:a, 0] = Y[0:a, 0] * 50

m = (U.shape)[1]
r = (Y.shape)[1]
par_na = 2
par_nb = 2

n = max(par_na,par_nb)

# additional params (ROB LS)
opt_dvaf = 10**(-6)
opt_max_iter = 10**2
opt_hst = 1

# MODEL 1 LS
mdl = lspm(U,Y,par_na,par_nb)
Ym1 = lspm_apl(U,Y,mdl,par_na,par_nb)

# MODEL 2 ROB LS
# roblspv returns a list of NumPy arrays which are later unpacked
model_list = roblspm(U,Y,par_na,par_nb,opt_dvaf,opt_max_iter,opt_hst)
# return_list = [PM,VAFw,VAF,YM,Pm]
mdl_PM = model_list[0]
mdl_VAFW = model_list[1]
mdl_VAF = model_list[2]
mdl_YM = model_list[3]
mdl_Pm = model_list[4]

Ym2 = lspm_apl(U,Y,mdl_Pm,par_na,par_nb)

vaf_model_1 = vaf( Y[a+n:][:], Ym1[a:][:])
print ('VAF MODEL 1')
for item in vaf_model_1:
    print ("--",item.round(3),"--",end='\n')


vaf_model_2 = vaf( Y[a+n:][:], Ym2[a:][:])
print ('VAF MODEL 2')
for item in vaf_model_2:
    print ("--",item.round(3),"--",end='\n')
    
    
# ADDITIONAL PLOT
    
    plt.title('RED = SALES, GREEN = ITERATIONS OF PM, \n\
              BLUE = MODEL 1, PURPLE = MODEL 2 (ROB_LS)')
    plt.xlabel('Days')
    plt.ylabel('Sales')
    # plots each iteration of PM
    h = mdl_PM.shape[1]
    for i in range(0,h):
        Ymi = dv2dm(mdl_YM[:,i],r)
        Ymi = Ymi[a+1:,:]
        plt.plot(Ymi, 'g',antialiased=True,linewidth = 0.5, alpha = 1)
    # plots Y
    Y_to_plot = Y[a+n:,:]
    plt.plot(Y_to_plot, 'r', antialiased = True, linewidth = 0.8)
    # plots Ym1
    Ym1_to_plot = Ym1[a:,:]
    plt.plot(Ym1_to_plot, 'b', antialiased = True, 
             linewidth = 3, alpha = 0.2)
    # plots Ym2
    Ym2_to_plot = Ym2[a:,:]
    plt.plot(Ym2_to_plot, 'm', antialiased = True, 
             linewidth = 3, alpha = 0.5)
  
    plt.show()