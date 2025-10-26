"""
Matrix Transformation
Medium
Linear Algebra

Write a Python function that transforms a given matrix A using the operation 
T**(-1)AS, where T and S are invertible matrices. The function should first validate if the matrices T and S are invertible, and then perform the transformation. In cases where there is no solution return -1

Example:
Input:
A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]
Output:
[[0.5,1.5],[1.5,3.5]]

"""

import numpy as np


def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    try:
        InvT = np.linalg.inv(T)
        InvS = np.linalg.inv(S)
    except np.linalg.LinAlgError:
        output = -1
    
    else:
        A_np = np.array(A)
        T_np = np.array(InvT)
        S_np = np.array(S)
        transformed_matrix = T_np @ A_np @ S_np
        output = transformed_matrix.tolist()
    
    return output