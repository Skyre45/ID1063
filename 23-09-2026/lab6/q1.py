import numpy as np

n = int(input("Enter no of elements: "))
a=[]
for i in range(n):
    val = float(input(f"Reading {i+1}: "))
    a.append(val)

def rms(a, n):
    a = np.array(a[:n])
    return np.sqrt(np.mean(a))

print(f"{rms(a, n):.2f}")



