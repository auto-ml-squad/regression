# -*- coding: utf-8 -*-
def vaf(Y, Ym):
    import numpy as np
    # takes two matrices
    # returns a vector
    # IGNORES WEIGHTS AND DEGREES OF FREEDOM
    
    # code in MATLAB
    # max(0, diag(eye(size(Y, 2)) - cov(Y - Ym)./cov(Y)))*100
    # first
    # eye(size(Y, 2))
    first = np.eye((Y.shape[1]))
    # second
    # cov(Y - Ym)./cov(Y)
    second_1 = Y - Ym
    second_1 = np.cov(second_1.transpose())
    second_2 = np.cov(Y.transpose())
    second = np.divide(second_1,second_2)
    # third
    # diag (first - second)
    third = np.diag(first-second)
    # fourth
    # max(0, third) * 100
    # why is MAX used with 0 as first argument?
    fourth = third * 100
    VAF = fourth
    
    return VAF
