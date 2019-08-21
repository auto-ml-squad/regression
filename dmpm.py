# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:58:09 2019

@author: Nikola
"""

def dmpm(U,Y,E,na=0,nb=0,nc=0,intercept=0):
    import numpy as np
    
    # assumes U,Y,E are not empty
    
    # a is a tuple of E's dimensions
    a = E.shape
    # N is E's rows; M is E's columns
    # used later when initializing empty arrays
    N = a[0]
    M = a[1]
    
    na = np.max(na)
    nb = np.max(nb)
    nc = np.max(nc)
    n = np.max(np.array([na,nb,nc]))
    
    
    if intercept:
        F = np.ones(((N-n),1))
    else:
        # WHAT SIZE ??
        F = np.empty([N,M])
        
    # in MATLAB several rows of each matrix (U,Y and E) are appended
    # F is returned at the end
    
    
    # shape of Y to append
    rows = Y.shape[0]
    cols = Y.shape[1]
    Y_to_append = np.empty([rows,cols])
    
    for i in range(na,1,-1):
        Y_to_append[i][:] = -Y[(n-na+i):(N-na+i-1)][:]
    # sticks Y to F
    np.concatenate(F,Y_to_append)
    
    # shape of U to append
    rows = U.shape[0]
    cols = U.shape[1]
    U_to_append = np.empty([rows,cols])
    
    for i in range(nb,1,-1):
        U_to_append[i][:] = U[(n-nb+i):(N-nb+i-1)][:]
    # sticks U to F
    np.concatenate(F,U_to_append)
    
    # shape of E to append
    rows = E.shape[0]
    cols = E.shape[1]
    E_to_append = np.empty([rows,cols])
    
    for i in range(nc,1,-1):
        E_to_append[i][:] = -E[(n-nc+i):(N-nc+i-1)][:]
    # sticks E to F
    np.concatenate(F,E_to_append)
        
    return F
    
        