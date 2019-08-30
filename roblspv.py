# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:33:28 2019

@author: Nikola
"""

def roblspv(
        U,Y,par_na,par_nb, 
        opt_dvaf = 10**(-2), 
        opt_max_iter = 100, 
        opt_hst = 0):
    
    from dmpv import dmpv
    from vaf import vaf
    from dv2dm import dv2dm
    
    r = (Y.shape)[1]
    na = par_na
    nb = par_nb
    n = max(int(np.max(par_na)),int(np.max(par_nb)))    
    
    # DATA MATRIX CREATION
    # TODO
    F = dmpv(U,Y,par_na,par_nb)
    
    
    
    # CODE IN MATLAB
    # pm = (F'*F)^-1 * F' * vec( Y(n + 1:end, :)');
    # first (F'*F)^-1
    first = np.dot(F.transpose(),F)
    first = np.linalg.inv(first)
    # second F'
    second = F.transpose()
    # third vec( Y(n + 1:end, :)')
    y = Y[(n):][:]
    y = y.transpose()
    y = y.flatten('F')
    
    pm = np.dot(first,second)
    pm = np.dot(pm,y)
    
    ym = np.dot(F,pm)
    
    # CODE IN MATLAB
    # vafw = vaf(dv2dm(y, r), dv2dm(ym, r));
    
    # TODO
    # dv2dm.py
    
    first = dv2dm(y,r)
    second = dv2dm(ym,r)
    
    vafw = vaf(first,second)
    vaf0 = vafw
    
    
    
    
    if opt_hst:
        VAFw = vafw
        VAF = vaf0
        PM = pm
        YM = ym
        
        