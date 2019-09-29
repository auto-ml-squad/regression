"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def wlspv(U,Y,W = 'no weights', par_na = 0, par_nb = 0):
    import numpy as np
    from numpy import linalg
    from dmpv import dmpv
    
    N,r = Y.shape
    na = par_na
    nb = par_nb
    n = max(int(np.max(par_na)),int(np.max(par_nb)))
    
    F = dmpv(U,Y,par_na,par_nb)
    
    if n == 0:
        pm = np.empty(shape = (0,0))
        return pm
    
    if W == 'no weights':
        print( "NO WEIGHTS!")
        pm = np.empty(shape = (0,0))
        return pm
    else:
        
        if r > W.shape[1]:
            # CODE IN MATLAB
            # W = diag(repmat(W(n + 1:end), r, 1));
            # the code in MATLAB creates a diagonal matrix with
            # size = W * r
            long_W = np.repeat(W[:-2][:], repeats = r, axis = 0)
            rep_W_mat = long_W * np.identity(len(long_W))
            
            W = rep_W_mat
        else:
            print("POSSIBLE CALCULATION PROBLEM")
            print("CHECK SHAPE OF W ARRAY!")
            short_W = W[:-2][:]
            rep_W_mat = short_W * np.identity(len(short_W))
            
            W = rep_W_mat
            
        # CODE IN MATLAB
        # pm = (F'*W'*F)^-1*F'*W*vec(Y(n + 1:end, :)');
        # first (F'*W'*F)^-1
        first_1 = np.dot(F.transpose() , W.transpose())
        first_2 = np.dot(first_1, F)
        first = np.linalg.inv(first_2)
        # second F'*W
        second = np.dot(F.transpose(),W)
        # third vec(Y(n + 1:end, :)')
        third = Y[2:][:]
        third = third.flatten()
        
        pm = np.dot(first,second)
        pm = np.dot(pm,third)
        
        return pm
        