# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:07:35 2019

@author: Nikola
"""

def lspv(U,Y,par_na,par_nb,par_mtype = 'sparse'):
    # returns the vector pm
    import numpy as np
    from numpy import linalg
    
    na = par_na
    nb = par_nb
    
    # EXPRESSION TO COMPUTE
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
    
    F = dmpv(U,Y,par_na,par_nb,par_nc = 0,par_mtype)