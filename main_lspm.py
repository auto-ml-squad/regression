# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:41:19 2019

@author: Nikola
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

vaf_model_1 = vaf( Y[n:][:], Ym1)

print ('VAF MODEL 1')
for item in vaf_model_1:
    print ("--",item.round(3),"--",end='\n')