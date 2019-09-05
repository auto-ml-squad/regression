# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:05:31 2019

@author: Nikola
"""

def roblspm(
        U,Y,par_na,par_nb, 
        opt_dvaf = 10**(-2), 
        opt_max_iter = 100, 
        opt_hst = 0):
    
    import numpy as np
    from numpy import linalg
    from dmpv import dmpv
    from dmpm import dmpm
    from vaf import vaf
    from dv2dm import dv2dm
    from pm2v import pm2v
    
    r = (Y.shape)[1]
    m = (U.shape)[1]
    na = par_na
    nb = par_nb
    n = max(na,nb)    
    
    # DATA MATRIX CREATION
    F = dmpm(U,Y,na,nb)
    # CODE IN MATLAB
    # Y = Y(n + 1:end, :);
    Y = Y[n:,:]
    # CODE IN MATLAB
    # Pm = (F'*F)^-1*F'*Y;
    # FIRST
    # (F'*F)
    F_transposed = F.transpose()
    first = np.dot(F_transposed,F)
    # SECOND
    # (F'*F)^-1
    second = np.linalg.inv(first)
    # THIRD
    # F'*Y
    third = np.dot(F_transposed,Y)
    # FOURTH
    # (F'*F)^-1*F'*Y;
    fourth = np.dot(second,third)
    Pm = fourth
    
    # CODE IN MATLAB
    # Ym = F*Pm;
    Ym = np.dot(F,Pm)
    
    vafw = vaf(Y,Ym)
    vaf0 = vafw
    
    
    # NEW VARIABLES
    
    if opt_hst:
        VAFw = vafw
        VAFw = VAFw.reshape(-1,1)
        VAF = vaf0
        VAF = VAF.reshape(-1,1)
        PM = pm2v(Pm,par_na,par_nb)
        PM = PM.reshape(-1,1)
        YM = Ym.flatten()
        YM = YM.reshape(-1,1)
        
    # -------------------------------------------------------------------    
    # START OF ITERATION LOOP
    iter = 0
    iterate = True
    
    while iterate:
        print("THIS IS ITERATION",iter+1)
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
        ww = np.broadcast_to(w,shape = (2176,F.shape[1]))
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
        pm = pm.reshape(-1,1)
        # ----------------------------------------------------------------
        # CODE IN MATLAB
        # ym = F*pm;
        ym = np.dot(F,pm)
        ym = ym.reshape(-1,1)
        
        vafw_1 = vafw
        
        # CODE IN MATLAB
        # vafw = vaf(dv2dm(y, r), dv2dm(ym, r), dv2dm(w, r));
        # vafw = vaf(Y          , Ym          , w          );
        vaf_arg_1 = dv2dm(y,r)
        vaf_arg_2 = dv2dm(ym,r)
        vaf_arg_3 = dv2dm(w,r)
        # vaf_weights FUNCTION NEEDED
        vafw = vaf(vaf_arg_1,vaf_arg_2,vaf_arg_3)
        vafw = vafw.reshape(-1,1)
        
        # CODE IN MATLAB
        # vaf0 = vaf(dv2dm(y, r), dv2dm(ym, r));
        vaf0 = vaf(vaf_arg_1,vaf_arg_2)
        vaf0 = vaf0.reshape(-1,1)
        
        if opt_hst :
            # appending values to arrays
            PM = np.append(PM,pm,axis = 1)
            VAFw = np.append(VAFw,vafw,axis = 1)
            VAF = np.append(VAF,vaf0,axis = 1)
            YM = np.append(YM,ym,axis = 1)
            
        # CHECK FOR END CONDITION
        # CODE IN MATLAB
        # if any(abs(vafw - vafw_1)) <= dvaf || iter >= maxIter, 
        if iter >= opt_max_iter:
            iterate = False
        else:
            # creating abs(vafw - vafw_1)
            vafw_differences = abs(np.subtract(vafw,vafw_1))
            for row in vafw_differences:
                for item in row:
                    if item <= opt_dvaf:
                        iterate = False
                    
    # CREATE RETURN LIST
    return_list = [PM,VAFw,VAF,YM,pm]
    
    return return_list