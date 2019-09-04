import numpy as np
def dmpm(U=0,Y=0,E=0, par={}):
    na=0
    nb=0
    nc=0
    
#first check if U,Y and E contain any data a.k.a are not empty matrices
    if U.size != 0: 
        dimension = np.shape(U)
        N = dimension[0]
    elif Y.size !=0:
        dimension = np.shape(Y)
        N = dimension[0]
    elif E.size !=0:
        dimension= np.shape(E)
        N= dimension[0]
    else: print('Error: At least one matrix should not be empty ')

#use dictionary for par.intercept ... par.nb and all -> par={'intercept':1,na:2,nb:2}    
#check for the existance of a key in a dictionary

    for k in par.keys():
        if "na" in par:
            na = par["na"]
        else:
            na= 0
        if "nb" in par:
            nb = par["nb"]
        else:
            nb= 0
        if "nc" in par:
            nc = par["nc"]
        else:
            nc= 0
#check if na,nb and nc are multidimensional arrays and if yes set each parameter to be the maximum value of the array vector             
        if  isinstance(na,np.ndarray):
            na = np.max(na)     
         
        if  isinstance(nb,np.ndarray):
            nb = np.max(nb)     
        
        if  isinstance(nc,np.ndarray):
            nc = np.max(nc)     
        
        n = np.max(np.array([na,nb]))

    
#next step is to form the matrix F

#first matrix that will be added to F. According to the results from the code in matlab Y matrix is added twice where first time it starts from the second row of Y and ends at last row-1
#second matrix that wil be added to F is the Y matrix starting from the first row and ending at last row-2
#first create empty matrices with the same dimension of Y. We will fill then concatenate them.       
             
    firstmatY= np.empty([(Y.shape[0]),(Y.shape[1])])
    secondmatY= np.empty([(Y.shape[0]),(Y.shape[1])])
    
    # first part
    for i in range(na,0,-1):
        firstmatY= -Y[(n-na+i):(N-na+i)][:]
        if i != na:    
            np.concatenate((firstmatY,firstmatY),axis = 1)
    # second part
    for i in range(na,0,-1):
        secondmatY= -Y[(n-na+i-1):(N-na+i-1)][:]
        if i != na:
             np.concatenate((secondmatY,secondmatY),axis = 1)
            
    F = np.concatenate((firstmatY,secondmatY),axis = 1)

    if nb == 0 :
        pass
    else:
        firstmatU= np.empty([(U.shape[0]),(U.shape[1])])
        secondmatU= np.empty([(U.shape[0]),(U.shape[1])])
        # first part
        for i in range(nb,0,-1):
            firstmatU = U[(n-nb+i):(N-nb+i)][:]
            if i != nb:    
                np.concatenate((firstmatU,firstmatU),axis = 1)
        # second part
        for i in range(nb,0,-1):
            secondmatU = U[(n-nb+i-1):(N-nb+i-1)][:]
            if i != nb:    
                np.concatenate((secondmatU,secondmatU),axis = 1)
                
        U = np.concatenate((firstmatU,secondmatU),axis = 1)    
        F = np.concatenate((F,U),axis = 1)
    

        
    return F