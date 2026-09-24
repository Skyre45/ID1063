def daysElapsed(day, month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    dE = sum(months[:month - 1])
    dE += day
    return dE

day, month = map(int, input().split())
print(daysElapsed(day, month))
