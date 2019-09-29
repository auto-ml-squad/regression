"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def lspm_apl(U,Y,Pm,par_na,par_nb):
    import numpy as np
    from dmpm import dmpm
    
    F = dmpm(U,Y,par_na,par_nb)
    Ym = np.dot(F,Pm)
    
    return Ym