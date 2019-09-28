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
from vaf import vaf

# CODE
# READING DATA

U = pd.read_csv('data/retail/U_new.csv',header = None).to_numpy()
Y = pd.read_csv('data/retail/Y.csv',header = None).to_numpy()

N,r = Y.shape
m = (U.shape)[1]
par_intercept = 0

# MODEL 1
par_na = 2
par_nb = 0
mdl1 = lspm(U,Y,par_na,par_nb)
# mdl1 e matrica
Ym1 = lspm_apl(U,Y,mdl1,par_na,par_nb)
#Ym1 e matrica
n = int(max( (par_na,par_nb)))

# MODEL 2
par_na = 2
par_nb = 2
mdl2 = lspm(U,Y,par_na,par_nb)
Ym2 = lspm_apl(U,Y,mdl2,par_na,par_nb)

# MODEL 3
par_na = 2
par_nb = 2
# in data > roll rows 1 up and duplicate last row
U = np.roll(U,-1,axis=0)
mdl3 = lspm(U,Y,par_na,par_nb)
Ym3 = lspm_apl(U,Y,mdl3,par_na,par_nb)

# MODEL 4
Ym4 = Ym3.clip(min=0)


n = int(max( (par_na,par_nb)))

vaf_model_1 = vaf( Y[n:][:], Ym1)
print ('VAF MODEL 1')
for item in vaf_model_1:
    print ("--",item.round(3),"--",end='\n')
    
vaf_model_2 = vaf( Y[n:][:], Ym2)
print ('VAF MODEL 2')
for item in vaf_model_2:
    print ("--",item.round(3),"--",end='\n')
    
vaf_model_3 = vaf( Y[n:][:], Ym3)
print ('VAF MODEL 3')
for item in vaf_model_3:
    print ("--",item.round(3),"--",end='\n')
    
vaf_model_4 = vaf( Y[n:][:], Ym4)
print ('VAF MODEL 4')
for item in vaf_model_4:
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
    y_mdl_3 = Ym3[:,col]
    y_mdl_4 = Ym4[:,col]
    
    plt.plot(x,y_data,alpha=0.3)
    plt.plot(x,y_mdl_1)
    plt.plot(x,y_mdl_2)
    plt.plot(x,y_mdl_3)
    plt.plot(x,y_mdl_4)
    
    plt.show()
    