"""
Write a program that accepts a positive integer n and prints an n × n
multiplication table.
For example, if n = 4, the output should be:
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
"""

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end = " ")
    print("\n")

