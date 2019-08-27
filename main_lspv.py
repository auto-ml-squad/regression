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
# TODO
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
pm = lspv(U,Y,par_na,par_nb)
# mdl1 e vektor
Ym1 = lspv_apl(U,Y,pm,par_na,par_nb)
#Ym1 vrushta matrica


## MODEL 2
par_na = np.ones((r,r)) * 2
par_nb = np.ones((r,m)) * 2
pm = lspv(U,Y,par_na,par_nb)
Ym2 = lspv_apl(U,Y,pm,par_na,par_nb)
#
## MODEL 3
#par_na = np.ones((r,r)) * 2
#par_nb = np.ones((r,m)) * 2
## in data > roll rows 1 up and duplicate last row
#U = np.roll(U,-1,axis=0)
#U[:][-1] = U[:][-2]
#mdl3 = lspv(U,Y,par_intercept,par_na,par_nb)
#Ym3 = lspv_apl(U,Y,mdl3)
#
## MODEL 4
## replaces all negative values with 0
#Ym4 = Ym3.clip(max=0)


n = int(max( (par_na.max(),par_nb.max())))

vaf_model_1 = vaf( Y[n:][:], Ym1)

vaf_model_2 = vaf( Y[(n):][:], Ym2)
#vaf_model_3 = vaf( Y[(n+1):][:], Ym1)
#vaf_model_4 = vaf( Y[(n+1):][:], Ym1)

# moje da se oformi tablica s matplotlib
print ('VAF MODEL 1')
for item in vaf_model_1:
    print ("--",item.round(2),"--",end='\n')
    
print ('VAF MODEL 2')
for item in vaf_model_2:
    print ("--",item.round(2),"--",end='\n')
    
#print ('VAF MODEL 3')
#print (vaf_model_3)
#print ('VAF MODEL 4')
#print (vaf_model_4)

# v matlab ima dopulnitelni plot-ove
# TODO
