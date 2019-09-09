# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:58:09 2019

@author: Nikola
"""
import numpy as np

def dmpm(U,Y,
         na = 0,
         nb = 0,
         nc = 0,
         E = np.empty(shape = (0,0))):
    import numpy as np
    # returns the matrix F
    
    # workflow choice
    U_present = False 
    Y_present = False 
    E_present = False
    
    # takes N depending on the matrices provided
    if np.sum(U) != 0:
        N = (U.shape)[0]
        U_present = True
    if np.sum(Y) != 0:
        N = (Y.shape)[0]
        Y_present = True
    if np.sum(E) != 0:
        N = (E.shape)[0]
        E_present = True

    na = int(np.max(na))
    nb = int(np.max(nb))
    nc = int(np.max(nc))
    n = np.max(np.array([na,nb,nc]))
    
    # ----------------------------------------------------------------- 
    # U and Y are provided as arguments
    # -----------------------------------------------------------------
    
    # in MATLAB several rows of each matrix (U and Y) are appended
    # number of columns doubles (???) 
    # [  starts at 1 ][  starts at 0  ]
    #          ...         ...
    # [ends at last-1][ends at last-2]
    if U_present and Y_present and not E_present:
        
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

    # ----------------------------------------------------------------- 
    # only E is provided as argument
    # -----------------------------------------------------------------
    if E_present and not U_present and not Y_present:
        
        rows = E.shape[0]
        cols = E.shape[1]
        E_to_append_1 = np.empty([rows,cols])
        E_to_append_2 = np.empty([rows,cols])
        
        # first part
        for i in range(nc,0,-1):
            E_to_append_1 = E[(n-nc+i):(N-nc+i)][:]
            if i != nc:    
                np.concatenate((E_to_append_1,E_to_append_1),axis = 1)
        # second part
        for i in range(nc,0,-1):
            E_to_append_2 = E[(n-nc+i-1):(N-nc+i-1)][:]
            if i != nc:    
                np.concatenate((E_to_append_2,E_to_append_2),axis = 1)
                
        F = np.concatenate((E_to_append_1,E_to_append_2),axis = 1)

    # ----------------------------------------------------------------- 
    # U, Y and E are provided as arguments
    # -----------------------------------------------------------------
    
    if U_present and Y_present and E_present:
        
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
            
        # ADDING E
        rows = E.shape[0]
        cols = E.shape[1]
        E_to_append_1 = np.empty([rows,cols])
        E_to_append_2 = np.empty([rows,cols])
        
        # first part
        for i in range(nc,0,-1):
            E_to_append_1 = E[(n-nc+i):(N-nc+i)][:]
            if i != nc:    
                np.concatenate((E_to_append_1,E_to_append_1),axis = 1)
        # second part
        for i in range(nc,0,-1):
            E_to_append_2 = E[(n-nc+i-1):(N-nc+i-1)][:]
            if i != nc:    
                np.concatenate((E_to_append_2,E_to_append_2),axis = 1)
                
        E = np.concatenate((E_to_append_1,E_to_append_2),axis = 1)
        F = np.concatenate((F,E),axis = 1)
        
    # ----------------------------------------------------------------- 
    # Returning F
    # -----------------------------------------------------------------
    
    return F
    
        