"""
Calculate Eigenvalues of a Matrix
Medium
Linear Algebra

Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.
"""

from math import sqrt, pow

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = matrix [0][0]
    b = matrix [0][1]
    c = matrix [1][0]
    d = matrix [1][1]

    eig_1 = ((a+d) + sqrt(pow(a,2)+(2*a*d)+pow(d,2)-(4*a*d)+(4*b*c))) / 2
    eig_2 = ((a+d) - sqrt(pow(a,2)+(2*a*d)+pow(d,2)-(4*a*d)+(4*b*c))) / 2

    eigenvalues = [eig_1, eig_2]
    
    return eigenvalues