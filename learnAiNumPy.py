import numpy as np

# From List
a = np.array([1, 2, 3, 4, 5, 6])

# All zeros
b = np.zeros(10)

# 2d array filled with 1 number c ((a, b), c)
c = np.full((4, 7), 5)

# display arrays
print(a)
print(b)
print(c)

# Generates an array a - b generated by a distance +c
d = np.arange(10, 100, 5)

# Generating equally spaced number a - b
e = np.linspace(start=1, stop=2, num=10)

# Generates random numbers in a 2-dimensional array
f = np.random.randint(5, 10, size=(3, 4))

# Generates random numbers 0 - 1
g = np.random.rand(10)

# display arrays
print(d)
print(e)
print(f)
print(g)

# Accessing the rows and columns of an array
h = np.random.randint(5, 10, size=(5, 5))

print(h)

# Access a single row and all following rows
print(h[1:])

# Access rows a - b
print(h[1:2])

# Access Columns [: ,a:b]
print(h[:, 1:3])

# Shapes and Reshapes
# Create an array of random numbers a - b
i = np.random.randint(1, 5, size=(4, 5))
print(i)

# Displays array size
print(i.shape)

# Displays array Area/volume
print(i.size)

# Displays Array Dimensionality
print(i.ndim)

# resize array to new shape
j = i.reshape(2, 10)
print(j)
print(j.shape)

# force array to a 1 dimensional array
k = j.ravel()
print(k)
print(k.shape)

# Convert 1-D array into 2-D Array -1 mean figure out how many rows/columns to give
k.reshape(-1, 1)
print(k)

# new axis means force another dimension
print(k[:, np.newaxis])

# Functions in numpy must use numpy functions
# Arranges numbers in an array in an evenly spaced
m = np.arange(5)
n = np.arange(6, 11)

# Concatonate arrays
print(m + n)

# take a sum
print(np.sum(m))
