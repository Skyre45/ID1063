"""
Write a program to accept two integers m and n and display the
perimeter of a m × n rectangle.
Example run:
Enter the value of m: 4
Enter the value of n: 7
"""
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

