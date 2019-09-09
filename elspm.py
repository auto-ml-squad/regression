# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:07:22 2019

@author: Nikola
"""

def elspm(U,Y,
          par_na = 0,
          par_nb = 0, 
          par_nc = 0,
          opt_maxiter = 50,
          opt_tauf = 10**(-6),
          opt_taux = 10**(-6),
          opt_dsp = 0):
    # returns a matrix and a vector
    
    import numpy as np
    from numpy import linalg
    from dmpm import dmpm
    from lspm import lspm
    import matplotlib.pyplot as plt
    
    na = par_na
    nb = par_nb
    nc = par_nc
    
    n = np.max([na,nb,nc])
    N,r = Y.shape
    nn = n - np.max([na,nb]) + 1
    
    modab = lspm(U,Y,na,nb)
    Pmab = modab
    Fab = dmpm(U,Y,na,nb,nc)
    
    # creating the E matrix
    E_first = np.zeros(shape = (n,r))
    E_second_1 = Y[n:,:]
    E_second_2 = np.dot(Fab,Pmab)
    E_second = E_second_1 - E_second_2
    # the E matrix will be added to the return list
    E = np.concatenate((E_first,E_second),axis = 0)
    
    # CODE IN MATLAB
    # f = sum(diag(E'*E)/N);
    first = np.dot(E.transpose(),E)
    second = np.diag(first)
    third = np.divide(second,N)
    f = np.sum(third)
    
    # START OF ITERATION LOOP
    # CODE IN MATLAB
    # Pm = [Pmab; zeros(r*nc, r)];
    Pm_top = Pmab
    Pm_bottom = np.zeros(shape = (r*nc,r))
    Pm = np.concatenate((Pm_top,Pm_bottom),axis = 0)
    iter = 0
    iterate = True
    
    while iterate:
        iter += 1
        F_top = Fab
        F_bottom = dmpm(U = np.zeros(shape = U.shape),
                    Y = np.zeros(shape = Y.shape),
                    na = 0, nb = 0, nc = nc,
                    E = E[:,:])
        F = np.concatenate((F_top,F_bottom),axis = 1)
        
        # checking step size (??)
        Pm_1 = Pm
        # CODE IN MATLAB
        # Pm = (F'*F)^-1*F'*Y(n + 1:N, :);
        # first (F'*F)^-1
        first = np.dot(F.transpose(),F)
        first = np.linalg.inv(first)
        # second F'
        second = F.transpose()
        # third Y(n + 1:N, :)
        third = Y[n:N][:]
        Pm = np.dot(first,second)
        Pm = np.dot(Pm,third)
        
        # CODE IN MATLAB
        # E = [zeros(n, r); Y(n + 1:end, :) - F*Pm];
        E_first = np.zeros(shape = (n,r))
        E_second_1 = Y[n:,:]
        E_second_2 = np.dot(F,Pm)
        E_second = E_second_1 - E_second_2
        # the E matrix will be added to the return list
        E = np.concatenate((E_first,E_second),axis = 0)

        
        f_1 = f
        # CODE IN MATLAB
        # f = sum(diag(E'*E)/N);
        first = np.dot(E.transpose(),E)
        second = np.diag(first)
        third = np.divide(second,N)
        f = np.sum(third)
        
#        print("f_1 = ",f_1)
#        print("f = ",f)
#        plt.figure()
#        plt.plot(F)
        
        if f > f_1 :
            Pm1 = Pm_1;
            Pm = Pm + Pm_1
            Pm = np.divide(Pm,2)
            # There should be a message here, warning for wrong step.
            # it should show if opt_dsp == 1
        
        # CHECKING FOR END CONDITION
        if iter >= opt_maxiter:
            iterate = False
        else:
            # CODE IN MATLAB
            # absXCONV = max(max(abs((x - x_1)./x_1)));
            # this part is skipped because of possible calculation
            # problems, values may be too large etc
            # runtime warnings appear
            
            # CODE IN MATLAB
            # absFCONV = abs(F_1 - F);
            absFCONV = np.abs(f_1 - f)
            if absFCONV < opt_tauf:
                iterate = False
    
    # END OF ITERATION LOOP
    if f > f_1:
        Pm = Pm1
    else:
        Pm = Pm
        
    # CREATING RETURN LIST
    elspm_list = [E,Pm]
    
    print("It took [elspm.py]",iter,"iterations to reach the end condition.")
    print(opt_maxiter,"is the maximum number of iterations.")
    return elspm_list