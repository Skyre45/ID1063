"""
Write a program that accepts a positive integer n, followed by n
floating-point values, and stores the values in an array.
Compute the average of the values and then print the number of values
that are strictly greater than the average.
For example:
Enter the value of n: 6
Enter the values: 4.5 2.0 7.5 5.0 3.0 8.0
Average: 5.0
Number of values above the average: 2
"""

import numpy as np

n = int(input("Enter the value of n: "))
arr = np.fromstring(input("Enter the values: "), sep=" ", dtype=float, count=n)

avg = np.mean(arr)
count = np.count_nonzero(arr > avg)

print(f"Average: {avg:.1f}")
print(f"Number of values above the average: {count}")

