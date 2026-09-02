"""
Write a program that accepts a positive integer n, followed by n in-
tegers stored in an array. Determine whether there are two distinct
positions in the array containing the same value.
If there are two such positions, print one such pair and the correspond-
ing common value. Otherwise, print that the array has no repeated
values.
For example:
Enter the value of n: 6
Enter the values: 4 7 2 9 7 5
Repeated value: 7, Positions: 1, 4
"""
import numpy as np

n = int(input("Enter the value of n: "))
arr = np.fromstring(input("Enter the values: "), sep=" ", dtype=int, count=n)

_, idx, counts = np.unique(arr, return_inverse=True, return_counts=True)
repeated_ids = np.flatnonzero(counts > 1)

if repeated_ids.size > 0:
    val = arr[idx == repeated_ids[0]][0]
    pos = np.flatnonzero(arr == val)
    print(f"Repeated value: {val}, Positions: {pos[0]}, {pos[1]}")
else:
    print("The array has no repeated values.")

