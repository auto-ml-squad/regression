"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def roblspm(
        U,Y,par_na,par_nb, 
        opt_dvaf = 10**(-2), 
        opt_max_iter = 100, 
        opt_hst = 0):
    
    import numpy as np
    from dmpm import dmpm
    from vaf import vaf
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
        iter += 1
        
        # ----------------------------------------------------------------
        # CODE IN MATLAB
        # ww = min(1, max(1e-8, abs(Y - Ym).^-1));
        # abs(y - ym).^-1
        first = np.absolute(np.subtract(Y,Ym))
        first = np.power(first,(-1))
        # max(1e-8, first) 
        second = np.clip(first, a_min = 10**(-8), a_max = np.max(first))
        # min(1,second)
        third = np.clip(second, a_min = np.min(first), a_max = 1)
        ww = third
        # ----------------------------------------------------------------
        for i in range(0,r):
            # Wi = repmat(ww(:, i), 1, r*na + m*nb);
            vctr = ww[:,i]
            Wi = np.tile(vctr,((r*na + m*nb),1)).transpose()
            # Pm(:, i) = (F'*(Wi.*F))^-1*F'*(ww(:, i).*Y(:, i));
            # first = (F'*(Wi.*F))^-1
            first_1 = F.transpose()
            first_2 = np.multiply(Wi,F)
            first_3 = np.dot(first_1,first_2)
            first_4 = np.linalg.inv(first_3)
            first = first_4
            # second = F'
            second = F.transpose()
            # third = (ww(:, i).*Y(:, i))
            third_1 = ww[:,i]
            third_2 = Y[:,i]
            third = np.multiply(third_1,third_2)
            # forming Pm
            Pm_1 = np.dot(first,second)
            Pm_2 = np.dot(Pm_1,third)
            Pm_final = Pm_2
            Pm[:,i] = Pm_final
            
        Ym = np.dot(F,Pm)
        vafw_1 = vafw
        vafw = vaf(Y,Ym,ww)
        vaf0 = vaf(Y,Ym)
        
        
        if opt_hst :
            # appending values to arrays
            to_append = pm2v(Pm,par_na,par_nb).reshape(-1,1)
            PM = np.append(PM,to_append,axis = 1)
            
            vafw = vafw.reshape(-1,1)
            VAFw = np.append(VAFw,vafw,axis = 1)
            
            vaf0 = vaf0.reshape(-1,1)
            VAF = np.append(VAF,vaf0,axis = 1)
            
            to_append = Ym.transpose().flatten('F').reshape(-1,1)
            YM = np.append(YM,to_append,axis = 1)
            
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
    
    print("The function [roblspm.py] took",iter,"iterations to reach the end condition.")
                    
    # CREATE RETURN LIST
    return_list = [PM,VAFw,VAF,YM,Pm]
    
    return return_list