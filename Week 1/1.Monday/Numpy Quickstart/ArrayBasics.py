# https://numpy.org/doc/stable/user/basics.creation.html
import numpy as np

def basics():
    a = np.array([1, 2, 3, 4, 5])
    print(a.dtype)

    b = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    print(b.dtype)

    c = np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)])

    d = np.array([[1, 2], [3, 4]], dtype=complex)
    print(d)

    # Always use np.array to create arrays and always define the dtype
def one_dimensional():
    print(
        np.arange(10) # Creates an array with values from 0 to 9
    )
    print(  
        np.arange(1, 2, 0.1)  # Creates an array with values from 1 to 2 with a step of 0.1
    )

    print(
        np.linspace(0, 1, 5)  # Creates an array with 5 values evenly spaced between 0 and 1
    )

def two_dimensional():
    print(
        np.eye(3)  # Creates a 3x3 identity matrix
    )

    print(
        np.diag([1, 2, 3])  # Creates a diagonal matrix with the given values on the diagonal
    )

def three_dimensional():
    print(
        np.zeros((2, 3, 4))  # Creates a 2x3x4 array filled with zeros
    )

    print(
        np.ones((2, 3, 4))  # Creates a 2x3x4 array filled with ones
    )

    print(
        np.full((2, 3, 4), 7)  # Creates a 2x3x4 array filled with the value 7
    )

def random_arrays():
    print(
        np.random.rand(2, 3)  # Creates a 2x3 array with random values from a uniform distribution over [0, 1)
    )

    print(
        np.random.randn(2, 3)  # Creates a 2x3 array with random values from a normal distribution
    )

    print(
        np.random.randint(0, 10, (2, 3))  # Creates a 2x3 array with random integers between 0 and 10
    )

