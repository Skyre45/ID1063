maxn = 0

n = int(input("number of numbers: "))

for i in range(n):
    a = float(input("number: "))
    if maxn < a:
        maxn = a

print("MAX NUMBER IS: ",maxn)
