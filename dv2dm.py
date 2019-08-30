# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:16:17 2019

@author: Nikola
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