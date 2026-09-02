"""
Write a program that accepts a positive integer n, followed by n inte-
gers, each between 0 and 9, and stores the values in an array. Print
the number of occurrences of each integer from 0 to 9.
For example:
Enter the value of n: 12
Enter the values: 3 1 4 1 5 9 2 6 5 3 5 1
"""
import numpy as np

n = int(input("Enter the value of n: "))

print("Enter the values: ", end="")
values = np.array(input().split(), dtype=int)

counts = np.bincount(values, minlength=10)

for digit in range(10):
    print(f"{digit}: {counts[digit]}")
