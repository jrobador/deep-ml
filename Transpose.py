#%%
# Write a Python function that computes the transpose of a given matrix.

#%%
result = []
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    for i in range(len(a[0])):
            result.append([a[j][i] for j in range(len(a))])
	
    return result