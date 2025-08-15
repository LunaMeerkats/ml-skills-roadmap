#https://numpy.org/doc/stable/user/basics.broadcasting.html#a-practical-example-vector-quantization

# Broadcasting rules:
# 1. If the arrays do not have the same number of dimensions, prepend the shape 
#       of the smaller-dimensional array with ones until both shapes have the same length.
# 2. The sizes of the dimensions must either be the same or one of them must be 1.
# 3. If the sizes of the dimensions do not match and neither is 1, an error is raised.
# 4. The result of the operation will have the shape of the larger array.

from numpy import array, argmin, sqrt, sum

observation = array ([111.0, 188.0])

codes = array ([
                [102.0, 203.0],
                [132.0, 193.0],
                [45.0, 155.0],
                [57.0, 173.0]
               ])

diff = codes - observation

# Why is the axis -1?
# The axis -1 refers to the last axis of the array, which is useful for operations
# that need to be performed across the last dimension of a multi-dimensional array.
dist = sqrt(sum(diff ** 2, axis=-1))

closest = argmin(dist)

print(f"Observation: {observation}")
print(f"Codes: {codes}")
print(f"Differences: {diff}")
print(f"Distances: {dist}")
print(f"Closest code: {codes[closest]}")

# Explaination of broadcasting:
# The operation `codes - observation` uses broadcasting to subtract 
# the 1D array `observation` from each row of the 2D array `codes`.
# Broadcasting allows NumPy to perform operations on arrays of different 
# shapes without needing to explicitly reshape them.