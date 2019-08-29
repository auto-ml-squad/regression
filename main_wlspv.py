# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:21:21 2019

@author: Nikola
"""

# LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# EXTERNAL FUNCTIONS
from lspv_apl import lspv_apl
from wlspv import wlspv
from vaf import vaf

# CODE
# READING DATA

U = pd.read_csv('data/retail/U_new.csv',header = None).to_numpy()
Y = pd.read_csv('data/retail/Y.csv',header = None).to_numpy()

N,r = Y.shape
m = (U.shape)[1]
par_intercept = 0

# WEIGHTS
W = np.ones(shape = (N,1))

# MODEL 1
par_na = np.ones((r,r)) * 2
par_nb = np.zeros((r,m))
mdl1 = wlspv(U,Y,W,par_na,par_nb)
# mdl1 e vektor
Ym1 = lspv_apl(U,Y,mdl1,par_na,par_nb)
#Ym1 e matrica

nn = max(int(np.max(par_na)),int(np.max(par_nb)))

vaf_model_1 = vaf( Y[nn:][:], Ym1)
print ('VAF MODEL 1')
for item in vaf_model_1:
    print ("--",item.round(3),"--",end='\n')