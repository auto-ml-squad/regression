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
    
    import numpy as np
    from numpy import linalg
    from dmpv import dmpv
    from vaf import vaf
    from dv2dm import dv2dm
    
    r = (Y.shape)[1]
    na = par_na
    nb = par_nb
    n = max(int(np.max(par_na)),int(np.max(par_nb)))    
    
    # DATA MATRIX CREATION
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
    
    first = dv2dm(y,r)
    second = dv2dm(ym,r)
    
    vafw = vaf(first,second)
    vaf0 = vafw
    
    # NEW VARIABLES
    
    if opt_hst:
        VAFw = vafw
        VAF = vaf0
        PM = pm
        YM = ym
        
    # ITERATION LOOP
    iter = 0
    iterate = True
    
    while iterate:
        iter += 1
        # ----------------------------------------------------------------
        # CODE IN MATLAB
        # w = min(1, max(1e-8, abs(y - ym).^-1));
        # abs(y - ym).^-1
        first = np.absolute(np.subtract(y,ym))
        first = np.power(first,(-1))
        # max(1e-8, first) 
        second = np.clip(first, a_min = 10**(-8), a_max = np.max(first))
        # min(1,second)
        third = np.clip(second, a_min = np.min(first), a_max = 1)
        w = third
        # ----------------------------------------------------------------
        # CODE IN MATLAB
        # ww = repmatc(w, size(F, 2));
        ww = np.broadcast_to(w,shape = (F.shape[1],2176)).transpose()
        # ----------------------------------------------------------------
        # CODE IN MATLAB
        # pm = (F'*(ww.*F))^-1*(ww.*F)'*y;
        # (F'*(ww.*F))^-1
        first = F.transpose()
        second = np.multiply(ww,F)
        third = np.dot(first,second)
        fourth = np.linalg.inv(third)
        # (ww.*F)'*y
        first = np.multiply(ww,F).transpose()
        second = np.dot(first,y)
        pm = np.dot(fourth,second)
        # ----------------------------------------------------------------
        ym = np.dot(F,pm)
        
        vafw_1 = vafw
        
        # CODE IN MATLAB
        # vafw = vaf(dv2dm(y, r), dv2dm(ym, r), dv2dm(w, r));
        # vafw = vaf(Y          , Ym          , w          );
        vaf_arg_1 = dv2dm(y,r)
        vaf_arg_2 = dv2dm(ym,r)
        vaf_arg_3 = dv2dm(w,r)
        # vaf_weights FUNCTION NEEDED
        
        
        
        
        
        