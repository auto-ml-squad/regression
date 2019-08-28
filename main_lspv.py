# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:54:57 2019

@author: Nikola
"""

# LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# EXTERNAL FUNCTIONS
from lspv_apl import lspv_apl
from lspv import lspv
from vaf import vaf

# CODE
# READING DATA

U = pd.read_csv('data/retail/U_new.csv',header = None).to_numpy()
Y = pd.read_csv('data/retail/Y.csv',header = None).to_numpy()

N,r = Y.shape
m = (U.shape)[1]
par_intercept = 0

# MODEL 1
par_na = np.ones((r,r)) * 2
par_nb = np.zeros((r,m))
mdl1 = lspv(U,Y,par_na,par_nb)
# mdl1 e vektor
Ym1 = lspv_apl(U,Y,mdl1,par_na,par_nb)
#Ym1 vrushta matrica

# MODEL 2
par_na = np.ones((r,r)) * 2
par_nb = np.ones((r,m)) * 2
mdl2 = lspv(U,Y,par_na,par_nb)
Ym2 = lspv_apl(U,Y,mdl2,par_na,par_nb)

# MODEL 3
par_na = np.ones((r,r)) * 2
par_nb = np.ones((r,m)) * 2
# in data > roll rows 1 up and duplicate last row
U = np.roll(U,-1,axis=0)
U[:][-1] = U[:][-2]
mdl3 = lspv(U,Y,par_na,par_nb)
Ym3 = lspv_apl(U,Y,mdl3,par_na,par_nb)

# MODEL 4
# replaces all negative values with 0
Ym4 = Ym3.clip(min=0)

n = int(max( (par_na.max(),par_nb.max())))

vaf_model_1 = vaf( Y[n:][:], Ym1)
vaf_model_2 = vaf( Y[(n):][:], Ym2)
vaf_model_3 = vaf( Y[(n):][:], Ym3)
vaf_model_4 = vaf( Y[(n):][:], Ym4)

# moje da se oformi tablica s matplotlib
print ('VAF MODEL 1')
for item in vaf_model_1:
    print ("--",item.round(3),"--",end='\n')
    
print ('\nVAF MODEL 2')
for item in vaf_model_2:
    print ("--",item.round(3),"--",end='\n')
    
print ('\nVAF MODEL 3')
for item in vaf_model_3:
    print ("--",item.round(3),"--",end='\n')
    
print ('\nVAF MODEL 4')
for item in vaf_model_4:
    print ("--",item.round(3),"--",end='\n')

# plot Y vs Y from Models
# Model 4 is unused (equivalent to Model 3)

for col in range(0,Y.shape[1]):
    title = str('Product '+str(col+1))
    
    plt.figure(col)
    
    plt.title(title)
    plt.xlabel('Days')
    plt.ylabel('Sales')
    
    x = range(0,Y.shape[0]-2)
    y_data = Y[:-2,col]
    
    y_mdl_1 = Ym1[:,col]
    y_mdl_2 = Ym1[:,col]
    y_mdl_3 = Ym1[:,col]
    
    plt.plot(x,y_data,alpha=0.3)
    plt.plot(x,y_mdl_1)
    plt.plot(x,y_mdl_2)
    plt.plot(x,y_mdl_3)
    
    plt.show()
    
    
    