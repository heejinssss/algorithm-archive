import sys

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
maxValue = lst[-1]
result = []

r = 2
while r <= maxValue:
    m = 0
    for num in lst:
        if (num % r == 0):
            m += 1
    result.append(m)
    r += 1

print(max(result))