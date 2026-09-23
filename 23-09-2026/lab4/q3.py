r = float(input("input roi"))

value =1
years = 0

while value<=2:
    value = value*((100+r)/100)
    years+=1

print("no of years = ",years)
