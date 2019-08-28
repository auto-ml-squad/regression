# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:19:23 2019

@author: Nikola
"""

def lspm_apl(U,Y,Pm,par_na,par_nb):
    import numpy as np
    from dmpm import dmpm
    
    F = dmpm(U,Y,par_na,par_nb)
    Ym = np.dot(F,Pm)
    
    return Ym