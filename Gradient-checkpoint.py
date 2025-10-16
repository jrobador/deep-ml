""" 
Gradient Checkpointing
Easy
Machine Learning


Problem
Write a Python function checkpoint_forward that takes a list of numpy functions (each representing a layer or operation) and an input numpy array, and returns the final output by applying each function in sequence. To simulate gradient checkpointing, the function should not store intermediate activations; instead, it should recompute them as needed (for this problem, just apply the functions in sequence as usual). Only use standard Python and numpy. The returned array should be of type float and have the same shape as the output of the last function.

 """
import numpy as np

def checkpoint_forward(funcs, input_arr):
    """
    Applies a list of functions in sequence to the input array, simulating gradient checkpointing by not storing intermediates.

    Args:
        funcs (list of callables): List of functions to apply in sequence.
        input_arr (np.ndarray): Input numpy array.

    Returns:
        np.ndarray: The output after applying all functions, same shape as output of last function.
    """
    output = input_arr
    for func in funcs:
        output = func(output)

    return output

#%%
import numpy as np
def f1(x): return x + 1
def f2(x): return x * 2
def f3(x): return x - 3
funcs = [f1, f2, f3]
input_arr = np.array([1.0, 2.0])
output = checkpoint_forward(funcs, input_arr)
print(output)
# %%
