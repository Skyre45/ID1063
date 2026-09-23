import math

def rms(a, n):
    a = a[:n]
    return round(math.sqrt(sum(map(lambda x: x**2 , a)) / n), 2)

n = int(input("Enter number of readings: "))
a = list(map(float, input("Enter readings: ").split()))

print(f"RMS = {rms(a, n):.2f}")
