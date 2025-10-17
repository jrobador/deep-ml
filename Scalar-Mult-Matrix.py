def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = [[el * scalar for el in ar] for ar in matrix]
    return result

matrix = [[1, 2], [3, 4]]
scalar = 2

print(scalar_multiply(matrix, scalar)) 