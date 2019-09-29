"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def lspm(U,Y,par_na = "nothing",par_nb = "nothing"):
    # returns a matrix
    
    import numpy as np
    from numpy import linalg
    from dmpm import dmpm
    
    if par_na == "nothing" and par_nb == "nothing":
        # CODE IN MATLAB
        # (U'*U)^-1*U'*Y
        
        # FIRST
        # (U'*U)
        U_transposed = U.transpose()
        first = np.dot(U_transposed,U)
        # SECOND
        # (U'*U)^-1
        second = np.linalg.inv(first)
        # THIRD
        # U'*Y
        third = np.dot(U_transposed,Y)
        # FOURTH
        # (U'*U)^-1*U'*Y
        fourth = np.dot(second,third)
        
        Pm = fourth
        #return Pm
    
    else:
        na = par_na
        nb = par_nb
        n = np.max([na,nb])
        N = Y.shape[0]
        
        if n == 0:
            Pm = np.empty(shape=(0,0))
            #return Pm
        
        F = dmpm(U,Y,na,nb)
        
        # CODE IN MATLAB
        # pm = (F'*F)^-1 * F' *  Y(n + 1:N, :)
        
        # first (F'*F)^-1
        first = np.dot(F.transpose(),F)
        first = np.linalg.inv(first)
        # second F'
        second = F.transpose()
        # third Y(n + 1:N, :)
        third = Y[n:N][:]
        
        Pm = np.dot(first,second)
        Pm = np.dot(Pm,third)
    
        return Pm
    