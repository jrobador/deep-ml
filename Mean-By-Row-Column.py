""" 
Calculate Mean by Row or Column
Easy
Linear Algebra


Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

 """
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    output = []
    if mode == 'row':
        for element in range(len(matrix)):
            mean_row = sum(matrix[element]) / len(matrix[element])
            output.append(mean_row)
    elif mode == 'column':
        for element in range(len(matrix[0])):
            sum_col = 0
            for row in matrix:
                sum_col += row[element]
            mean_col = sum_col / len(matrix)
            output.append(mean_col)

    else: 
        raise ValueError("Mode must be 'row' or 'column'")
    
    return output

print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'row'))
