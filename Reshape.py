#%%
def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    total = len(a) * len(a[0])
    if (new_shape[0] * new_shape[1]) != total:
        return []

    flat_list = [item for sublist in a for item in sublist]
    result = []
    internal_array = []
    internal_pointer_variable = 0

    for i in (flat_list):
        internal_array.append(i)
        internal_pointer_variable += 1
        if internal_pointer_variable == new_shape[1]:
            result.append(internal_array)
            internal_array = []
            internal_pointer_variable = 0

    return result

# Version limpia con mejor manejo del for
def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    total_elements = len(a) * len(a[0])
    
    if new_shape[0] * new_shape[1] != total_elements:
        return []

    flat = [x for row in a for x in row]

    reshaped = []
    for i in range(0, total_elements, new_shape[1]):
        reshaped.append(flat[i:i + new_shape[1]])

    return reshaped


# Con numpy
import numpy as np

def reshape_matrix_np(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    arr = np.array(a)
    try:
        reshaped = arr.reshape(new_shape)
        return reshaped.tolist()
    except ValueError:
        return []