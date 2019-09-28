"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def lspv(U,Y,par_na,par_nb):
    # returns the vector pm
    import numpy as np
    from numpy import linalg
    from dmpv import dmpv
    
    na = par_na
    nb = par_nb
    
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
    
    pm = fourth
    
    n = np.max([np.max(na),np.max(nb)])
    
    F = dmpv(U,Y,par_na,par_nb)
    # CODE IN MATLAB
    # pm = (F'*F)^-1 * F' * vec( Y(n + 1:end, :)');
    # first (F'*F)^-1
    first = np.dot(F.transpose(),F)
    first = np.linalg.inv(first)
    # second F'
    second = F.transpose()
    # third vec( Y(n + 1:end, :)')
    third = Y[(n):][:]
    third = third.transpose()
    third = third.flatten('F')
    
    pm = np.dot(first,second)
    pm = np.dot(pm,third)
    
    return pm