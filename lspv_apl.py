# -*- coding: utf-8 -*-

def lspv_apl(U,Y,pm,par_na,par_nb):
    import numpy as np
    from pv2m import pv2m
    from dmpm import dmpm
    
    Pm = pv2m(pm,par_na,par_nb)
    F = dmpm(U,Y,par_na,par_nb)
    
    Ym = np.dot(F,Pm)
    
    return Ym