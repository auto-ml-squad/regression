"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
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
    y = y.reshape(-1,1)
    
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
        VAFw = VAFw.reshape(-1,1)
        VAF = vaf0
        VAF = VAF.reshape(-1,1)
        PM = pm
        PM = PM.reshape(-1,1)
        YM = ym
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
    
        
        
        
        
        
        