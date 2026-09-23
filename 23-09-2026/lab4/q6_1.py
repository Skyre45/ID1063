n = int(input("number: "))
count = 0

while n != 0:
    print(n)
    count+=1
    n = n//10

print("Number of iterations were: ",count)

