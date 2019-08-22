# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:40:10 2019

@author: Nikola
"""

def dmpv(U,Y,par_na,par_nb,par_nc = 0,par_intercept = 0, par_mtype):
    # returns the matrix F
    import numpy as np

    # this function has two parts
    # according to the type of matrix (full or sparse)
    # in our case only the sparse portion runs
    
    # only the sparse matrix case is converted to python
    
    # START OF YY
    for i in range(0,r):
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
    # in MATLAB this never runs (nb is all zeros)
        for j in range(0, m):
            if par_nb[i][j] > 0:
                Ui = U.transpose()[:][j]

# first [1:N - n]'*ones(1, nc(i, j))
                first = np.arange(1,(N-n+1))
                first = first.transpose()
                second = np.ones(shape=(1,int(par_nc[i][j])))
                third_1 = np.tile(first,(2,1)).transpose() * second
# second ones(N - n, 1)*[0:-1:-(nc(i, j) - 1)]
                first = np.ones(shape=((N-n),1))
                second = np.arange(0,-(par_nc[i][j]),-1)
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
        # to vector
        # v MATLAB se suzdava sparse matrix
        # kak se suzdava sparse matrica v python / numpy ??
        YUE = -YY.flatten('F')
        
        
        
        

    
            
                    
