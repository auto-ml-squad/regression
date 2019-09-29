"""
author: OPEN-MAT
date: 	15.06.2019
Matlab version: 26 Apr 2009
Course: Multivariable Control Systems
"""
def dv2dm(v,cols):
    import numpy as np
     
    # CHECK FOR CORRECT SHAPE
    if v.shape[0] % cols != 0:
        print("INCORRECT MATRIX DIMENSIONS")
        return "error"
    
    # MATRIX DIMENSIONS
    mat_rows = int(v.shape[0] / cols)
    mat_cols = cols
    
    # CREATE BASE MATRIX
    dm = np.ones(shape=(mat_rows,mat_cols))
    
    current_pos = 0
    for row in range(0,mat_rows):
        for column in range(0,mat_cols):
            dm[row][column] = v[current_pos]
            current_pos += 1
            
    return dm