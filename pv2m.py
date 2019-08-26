# -*- coding: utf-8 -*-

def pv2m(pm,par_na,par_nb = 0):
    import numpy as np
    
    # returns a matrix
    # (reshaped pm vector)
    
    # razlika s MATLAB (nqma zna4enie)
    na = int(par_na[0][0])
    nb = int(par_nb[0][0])
    
    [r,m] = par_nb.shape
    r = int(r); m = int(m)
    
    
    nna = int(np.max(np.max(na)))
    nnb = int(np.max(np.max(nb)))
    
    z = int(r*nna + m*nnb)
    
    Pm = np.zeros(shape = (r,z))
    ii = 0
    correction = 0
    
    for i in range(0,r):
        if nna:
            for j in range(0,r):
                Pm[i][j] = pm[j+ii-correction+i*5]
                Pm[i][j+r] = pm[j+ii+1-correction+i*5]
                
                correction += 1
                ii += 2
        
        # MAY NEED TO ADD THE U MATRIX LATER
        
    return Pm.transpose()
                
                