# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:40:10 2019

@author: Nikola
"""

def dmpv(U,Y,par_na,par_nb,par_nc = 0,par_intercept = 0, par_mtype = 0):
    # returns the matrix F
    # NO SPARSE MATRICES USED/IMPLEMENTED
    # does not use par_nc, EE etc.
    import numpy as np
    
    m = (U.shape)[1]
    N,r = Y.shape
    n = int(np.max([np.max(par_na),np.max(par_nb)]))
    na = par_na
    nb = par_nb
    
    # used in the creation of the Fi matrix
    # initialized here
    # clean later
    current_row = 0
    
    
    for i in range(0,r):
    # START OF YY
        for j in range(0, (r + par_intercept)):
            if par_na[i][j] > 0:
                Yi = Y.transpose()[:][j]
# code in MATLAB
# YY = [YY Yi([1:N - n]'*ones(1, na(i, j)) + ones(N - n, 1)*[0:-1:-(na(i, j) - 1)] + n - 1)]; 
# appends two columns to YY
# some kind of range inside the brackets -> Yi()
# ?????????????
# first [1:N - n]'*ones(1, na(i, j))
                first = np.arange(1,(N-n+1))
                first = first.transpose()
                second = np.ones(shape=(1,int(par_na[i][j])))
                third_1 = np.tile(first,(2,1)).transpose() * second
# second ones(N - n, 1)*[0:-1:-(na(i, j) - 1)]
                first = np.ones(shape=((N-n),1))
                second = np.arange(0,-(par_na[i][j]),-1)
                third_2 = np.tile(first,(1,2)) * second
# third first + second + n - 1
                third_3 = third_1 + third_2 + n - 1
# final
                # third_3 sluji kato nqkakav ukazatel za indeksi
                # novoto Yi se zapulva sus stoinosti sprqmo third_3
                rows,cols = third_3.shape
                for x in range(rows):
                    for y in range(cols):
                        third_3[x][y] = Yi[int(third_3[x][y]-1)]
                Yi_to_append = third_3
                # YY starts off empty and grows in size each iteration
                if j == 0:    
                    YY = Yi_to_append
                else:
                    YY = np.concatenate((YY,Yi_to_append),axis = 1)
                    # ¡SUVPADA S MATLAB!
                                   
    # START OF UU
        for j in range(0, m):
            if par_nb[i][j] > 0:
                Ui = U.transpose()[:][j]

# first [1:N - n]'*ones(1, nc(i, j))
                first = np.arange(1,(N-n+1))
                first = first.transpose()
                second = np.ones(shape=(1,int(par_nb[i][j])))
                third_1 = np.tile(first,(2,1)).transpose() * second
# second ones(N - n, 1)*[0:-1:-(nc(i, j) - 1)]
                first = np.ones(shape=((N-n),1))
                second = np.arange(0,-(par_nb[i][j]),-1)
                third_2 = np.tile(first,(1,2)) * second
# third first + second + n - 1
                third_3 = third_1 + third_2 + n - 1
# final
                rows,cols = third_3.shape
                for x in range(rows):
                    for y in range(cols):
                        third_3[x][y] = Ui[int(third_3[x][y]-1)]
                Ui_to_append = third_3

                if j == 0:    
                    UU = Ui_to_append
                else:
                    UU = np.concatenate((UU,Ui_to_append),axis = 1)
            else:
                UU = 0
                
                    
        # suzdavane na F matrica, sudurja6ta YY i UU
        if par_nb[i][j] > 0:
            YYUU = np.concatenate((-YY,UU),axis = 1)
        else:
            YYUU = -YY
        
        pi = int(np.sum(na[i][:]) + np.sum(nb[i][:]))
        Fi = np.zeros(shape=(int(((N-n))*r),pi))
        
        # code in MATLAB
        # Fi (i:r:(N-n)*r, 1:pi) = [-YY UU];
        
        for item in range(i,(N-n)*r,r):          
            Fi[item][:] = YYUU[current_row][:]
            current_row += 1
            if current_row == (N-n):
                current_row = 0
                
        if i == 0:
            F = Fi
        else:
            F = np.concatenate((F,Fi),axis = 1)
        
    return F