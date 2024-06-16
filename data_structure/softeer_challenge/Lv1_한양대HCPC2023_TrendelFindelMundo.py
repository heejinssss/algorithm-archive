import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * n
for i in range(n):
    a, b = map(int,input().split())
    lst[i] = [a, b]

comp1 = 0
comp2 = 1001
for l in lst:
    if comp2 > l[1]:
        comp1 = l[0]
        comp2 = l[1]
        
print(comp1, comp2)