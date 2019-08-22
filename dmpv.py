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
    
    # the initial sizes of the matrices here are taken
    # from MATLAB after running the whole function
    # NOT GOOD! 
    # matrices should be dinamically created
    
    F = np.empty(shape = (5440,50))
    
    for i in range(0,r):
        YY = np.empty((1088,10))
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
                                   
                                   
# this repeats several times
               
# testing
