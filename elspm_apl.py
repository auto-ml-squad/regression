# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:44:45 2019

@author: Nikola
"""

def elspm_apl(U,Y,Pm,par_na,par_nb,par_nc,E):
    import numpy as np
    from dmpm import dmpm
    
    F = dmpm(U,Y,par_na,par_nb,par_nc,E)
    Ym = np.dot(F,Pm)
    
    return Ym