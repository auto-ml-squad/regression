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
from elspm_apl import elspm_apl
from lspm import lspm
from elspm import elspm
from vaf import vaf

# CODE
# READING DATA

U = pd.read_csv('data/retail/U_new.csv',header = None).to_numpy()
Y = pd.read_csv('data/retail/Y.csv',header = None).to_numpy()

N,r = Y.shape
m = (U.shape)[1]
par_na = 2
par_nb = 2
par_nc = 2
par_intercept = 0

# MODEL 1
mdl1 = lspm(U,Y,par_na,par_nb)
# mdl1 e matrica
Ym1 = lspm_apl(U,Y,mdl1,par_na,par_nb)
#Ym1 e matrica
Pm1_zeros = np.zeros(shape = ((r*par_nc),r))
Pm = np.concatenate((mdl1,Pm1_zeros),axis = 0)

n = int(max( (par_na,par_nb)))

# MODEL 2
opt_maxiter = 50
opt_taux = 10**(-6)
opt_tauf = 10**(-6)
opt_dsp = 0

# the list contains the matrix E and a vector Pm
elspm_list = elspm(U,Y,par_na,par_nb,par_nc)
E = elspm_list[0]
Pm = mdl2 = elspm_list[1]
Ym2 = elspm_apl(U,Y,Pm,par_na,par_nb,par_nc,E)

n = int(max( (par_na,par_nb,par_nc)))

vaf_model_1 = vaf( Y[n:][:], Ym1)
print ('VAF MODEL 1')
for item in vaf_model_1:
    print ("--",item.round(3),"--",end='\n')
    
vaf_model_2 = vaf( Y[n:][:], Ym2)
print ('VAF MODEL 2')
for item in vaf_model_2:
    print ("--",item.round(3),"--",end='\n')
    
# plot Y vs Y from Models

for col in range(0,Y.shape[1]):
    title = str('Product '+str(col+1))
    
    plt.figure(col)
    
    plt.title(title)
    plt.xlabel('Days')
    plt.ylabel('Sales')
    
    x = range(0,Y.shape[0]-2)
    y_data = Y[:-2,col]
    
    y_mdl_1 = Ym1[:,col]
    y_mdl_2 = Ym2[:,col]
    
    plt.plot(x,y_data,alpha=0.3)
    plt.plot(x,y_mdl_1)
    plt.plot(x,y_mdl_2)
    
    plt.show()