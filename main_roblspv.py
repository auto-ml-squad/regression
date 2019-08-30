# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:33:27 2019

@author: Nikola
"""

# LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# EXTERNAL FUNCTIONS
from lspv_apl import lspv_apl
from lspv import lspv
from roblspv import roblspv
from vaf import vaf

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
par_na = np.ones((r,r)) * 2
par_nb = np.ones((r,m)) * 2

n = max(int(np.max(par_na)),int(np.max(par_nb)))

# MODEL 1
mdl = lspv(U,Y,par_na,par_nb)
Ym1 = lspv_apl(U,Y,mdl,par_na,par_nb)

# additional params
opt_dvaf = 10**(-6)
opt_max_iter = 10**(2)
