# -*- coding: utf-8 -*-

def pv2m(pm,par_na = 0,par_nb = 0, par_nc = 0):
    import numpy as np
    # IGNORES INTERCEPT
    
    #CONVERT COLUMN TO 2D ARRAY WITH 1 COLUMN
    pm = pm.reshape(-1,1)
    r,m = par_nb.shape
    
    nna = int(np.max(par_na))
    nnb = int(np.max(par_nb))
    nnc = int(np.max(par_nc))
    
    z = r * nna + m * nnb + r * nnc
    
    Pm = np.zeros(shape = (r,z))
    
    # in Python: [START : STOP : STEP]
    ii = 0
    
    for i in range(0,r):
        # NNA
        if nna:
            for j in range(0,r):
                Pm[i,0+j:int(par_na[i,j]*r -1+j):r] = \
                pm[int(0+ii):int(par_na[i,j]+ii),0]
                ii += par_na[i,j]
        # NNB
        if nnb:
            for j in range(0,m):
                Pm[i, 0+j+r*nna:int(par_nb[i,j]*m -1+j+r*nna):m] = \
                pm[int(0+ii):int(par_nb[i,j]+ii),0]
                ii += par_nb[i,j]
        # NNC
        if nnc:
            for j in range(0,r):
                Pm[i, 0+j+r*nna+m*nnb:int(par_nc[i,j]*r -1+j+r*nna+m*nnb):r] = \
                pm[int(0+ii):int(par_nc[i,j]+ii),0]
                ii += par_nc[i,j]
            
    return Pm.transpose()