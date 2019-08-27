# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:58:09 2019

@author: Nikola
"""

def dmpm(U,Y,na = 0,nb = 0,intercept = 0):
    import numpy as np
    # returns the matrix F
    # E is not used
    # assumes U,Y are not empty
    N,r = Y.shape
    
    na = int(np.max(na))
    nb = int(np.max(nb))
    
    n = np.max(np.array([na,nb]))
    
        
    # in MATLAB several rows of each matrix (U and Y) are appended
    # number of columns doubles (???) 
    # [  starts at 1 ][  starts at 0  ]
    #          ...         ...
    # [ends at last-1][ends at last-2]
    
    rows = Y.shape[0]
    cols = Y.shape[1]
    Y_to_append_1 = np.empty([rows,cols])
    Y_to_append_2 = np.empty([rows,cols])
    
    # first part
    for i in range(na,0,-1):
        Y_to_append_1 = -Y[(n-na+i):(N-na+i)][:]
        if i != na:    
            np.concatenate((Y_to_append_1,Y_to_append_1),axis = 1)
    # second part
    for i in range(na,0,-1):
        Y_to_append_2 = -Y[(n-na+i-1):(N-na+i-1)][:]
        if i != na:    
            np.concatenate((Y_to_append_2,Y_to_append_2),axis = 1)
            
    F = np.concatenate((Y_to_append_1,Y_to_append_2),axis = 1)

    # U doesnt run in MATLAB for model_1
    if nb == 0 :
        pass
    else:
        rows = U.shape[0]
        cols = U.shape[1]
        U_to_append_1 = np.empty([rows,cols])
        U_to_append_2 = np.empty([rows,cols])
        
        # first part
        for i in range(nb,0,-1):
            U_to_append_1 = U[(n-nb+i):(N-nb+i)][:]
            if i != nb:    
                np.concatenate((U_to_append_1,U_to_append_1),axis = 1)
        # second part
        for i in range(nb,0,-1):
            U_to_append_2 = U[(n-nb+i-1):(N-nb+i-1)][:]
            if i != nb:    
                np.concatenate((U_to_append_2,U_to_append_2),axis = 1)
                
        U = np.concatenate((U_to_append_1,U_to_append_2),axis = 1)    
        F = np.concatenate((F,U),axis = 1)
    

        
    return F
    
        