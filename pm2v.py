"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def pm2v(Pm,par_na = 0,par_nb = 0):
    # IGNORES NC
    # RETURNS A VECTOR
    import numpy as np
    
    na = par_na
    nb = par_nb
    # R and M inherits the shape of nb
    # nb is integer so both are = 1
    r = m = 1
    z = na + nb
    
    if z == 0:
        pm = np.empty(shape = (1,1))
        return pm
    # na and nb are integers so there is no MAX value
    # MAY NEED REWRITING
    nna = na
    nnb = nb
    
    # empty array that grows in a vector
    pm = np.array(())
    
    for i in range(0,r):
        #print("ITERATION")
        pari = Pm[:,i]
        if nna > 0:
            for j in range(0,r):
                # CODE IN MATLAB
                # pij = [pari(j:r:r*(na(i, j) - 1) + j)];
                # in Python: [START : STOP : STEP]
                pij = pari[j+j:r*na+j:r]
                # pm = [pm; pij];
                pm = np.concatenate((pm,pij),axis=0)
        if nnb > 0:
            for j in range(0,m):
                pij = pari[j+j+r*nna:m*nb+j+r*nna:m]
                pm = np.concatenate((pm,pij),axis=0)
                
    return pm
                
                