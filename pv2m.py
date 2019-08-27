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

    
    if nnb >= nna:
            # NOT GOOD
            # REWRITING NEEDED
            # NOT GOOD
            
            first_row_indexes = [0,2,4,6,8,1,3,5,7,9,10,12,14,16, \
                                 18,20,22,24,26,28,30,32,11,13, \
                                 15,17,19,21,23,25,27,29,31,33]
            for i in first_row_indexes:
                Pm[0][i] = pm[first_row_indexes[i]]
            for i in range(1,r):
                for x in range(0,34):
                    Pm[i][x] = pm[first_row_indexes[x] + 34*i]
            
            # NOT GOOD
            # REWRITING NEEDED
            # NOT GOOD
            return Pm.transpose()
    else:
        ii = 0
        correction = 0
        
        for i in range(0,r):
            for j in range(0,r):
                Pm[i][j] = pm[j+ii-correction+i*5]
                Pm[i][j+r] = pm[j+ii+1-correction+i*5]
                
                correction += 1
                ii += 2
        
        return Pm.transpose()
                
                