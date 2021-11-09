

# using numpy
import numpy as np
def product_np(arr):
    return [np.prod(arr)/x for x in arr]

#using builtin reduce
from functools import reduce
def product_reduce (arr):
    return [reduce((lambda x, y: x * y),arr) / i for i in arr]
    
#without division ? 
def product_nodiv(arr):
    output= []
    for e in arr:
        new_array = list(arr)
        new_array.remove(e)
        output.append(reduce((lambda x, y: x * y),new_array))
    return output


#tests
assert product_np([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_np([3, 2, 1]) == [2, 3, 6]
assert product_nodiv([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_nodiv([3, 2, 1]) == [2, 3, 6]