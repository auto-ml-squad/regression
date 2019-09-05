# -*- coding: utf-8 -*-
import numpy as np
def vaf(Y, Ym,
        w = np.empty(shape=(0,0))
        ):
    # returns a vector
    # IGNORES DEGREES OF FREEDOM
    # ----------------------------------------------------------------
    # NO WEIGHTS PROVIDED
    if w.shape[0] == w.shape[1] == 0:
        #print("NO WEIGHTS")
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
        fourth = np.clip(third, a_min = 0, a_max = np.max(third)) * 100
        # why is MAX used with 0 as first argument?
        #fourth = third * 100
        VAF = fourth
        
        return VAF
    # ----------------------------------------------------------------
    # WEIGHTS ARE PROVIDED
    
    # CODE IN MATLAB
    # if nargin == 3 && all(size(Y) == size(w))
    if (Y.shape == w.shape):
        p = 0
        
    [N,r] = Y.shape
    # Nw = sum(w)';
    Nw = np.sum(w,axis = 0).transpose()
    # if size(w, 2) < r, 
    # w = repmat(w, 1, r); 
    if w.shape[1] < r:
        #print("SHAPE CHANGED")
        w = np.broadcast_to(w,shape = (1,r))
        
    #    mY = sum(Y.*w)'./Nw;
    first = np.multiply(Y,w)
    second = np.sum(first, axis = 0).transpose()
    third = np.divide(second,Nw)
    mY = third
    #    E = Y - Ym;
    E = Y - Ym
    #    Yc = Y - repmat(mY', N, 1);
    first = np.ones(shape = (N,mY.shape[0]))
    for row in range(0,first.shape[0]):
        first[row][:] = mY[:]
    Yc = np.subtract(Y,first)
    
    #    SSE = sum(E.*(E.*w))';
    # PRECISION PROBLEMS HERE
    first = np.zeros(shape = E.shape)
    for row in range(0,E.shape[0]):
        for col in range(0,E.shape[1]):
            first[row][col] = np.multiply(round(E[row][col],5),round(w[row][col],5))
    # PRECISION PROBLEMS HERE
    second = np.multiply(E,first)
    third = np.sum(second,axis = 0).transpose()
    SSE = third
    
    #    SST = sum(Yc.*(Yc.*w))';
    first = np.zeros(shape = Yc.shape)
    for row in range(0,Yc.shape[0]):
        for col in range(0,Yc.shape[1]):
            first[row][col] = np.multiply(round(Yc[row][col],5),round(w[row][col],5))
    # PRECISION PROBLEMS HERE
    second = np.multiply(Yc,first)
    third = np.sum(second,axis = 0).transpose()
    SST = third
    
    # CODE IN MATLAB
    # VAF = max(zeros(r, 1), 100*(ones(r, 1) - (SSE./(Nw - p - 1))./(SST./(Nw - 1))));
    #first = (SSE./(Nw - p - 1));
    first = np.divide(SSE,(Nw - p - 1))
    #second = (SST./(Nw - 1));
    second = np.divide(SST,(Nw -1 ))
    #third = first ./ second;
    third = np.divide(first,second)
    #fourth = 100*(ones(r,1) - third);
    fourth = np.multiply(100,(np.subtract(np.ones(shape=(r,1)),third)))
    fourth = fourth[0][:]
    #fifth = max( zeros(r,1), fourth);
    fifth = np.clip(fourth,a_min=0,a_max = np.max(fourth))
    
    VAF = fifth
    
    return VAF
    
    
    
        
    
    
    
        
