"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def lspv_apl(U,Y,pm,par_na,par_nb):
    import numpy as np
    from pv2m import pv2m
    from dmpm import dmpm
    
    Pm = pv2m(pm,par_na,par_nb)
    F = dmpm(U,Y,par_na,par_nb)
    
    Ym = np.dot(F,Pm)
    
    return Ym