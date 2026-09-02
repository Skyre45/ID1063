"""
Write a program to accept a positive integer n, two vectors of length
n into two arrays, and find their dot product. Example run:
Enter the value of n: 5
Enter the values of the first vector: 3 -1 10 2.5 6
Enter the values of the second vector: 0.5 4 1 0 -0.5
The dot product is 4.5.
"""
import numpy as np

vec1 = np.loadtxt("vec1.dat")
vec2 = np.loadtxt("vec2.dat")

dot_product = np.dot(vec1, vec2)

print(f"The dot product is {dot_product}.")
