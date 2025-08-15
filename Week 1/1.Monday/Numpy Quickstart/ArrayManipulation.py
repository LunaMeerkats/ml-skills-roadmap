import numpy as np

a = np.array([1, 2, 3, 4, 5])

b = a[:2].copy()  # Creates a copy of the first two elements of array a
b += 1 # Increments each element of b by 1

print(b)  # Prints the modified copy of a


A = np.ones((2, 2))  # Creates a 2x2 array filled with ones
B = np.eye(2)  # Creates a 2x2 identity matrix
C = np.zeros((2, 2))  # Creates a 2x2 array filled with zeros
D = np.diag([-3, -4])  # Creates a diagonal matrix with the given values on the diagonal
E = np.block([[A, B], [C, D]])  # Combines the arrays into a block matrix
print(E)  # Prints the combined block matrix
