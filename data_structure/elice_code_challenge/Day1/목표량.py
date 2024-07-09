import itertools
import heapq

N = input() # string

nPr = itertools.permutations(N, len(N))
nList = list(nPr)
nJoinList = []

tmp = []
for numbers in nList:
    heapq.heappush(tmp, "".join(numbers))

for _ in range(len(tmp)):
    heapq.heappush(nJoinList, heapq.heappop(tmp))

answer = '999999'

for i in range(-1, len(nJoinList)-1):
    if nJoinList[i] == N and nJoinList[i+1] != N:
        answer = "".join(nJoinList[i+1])
        break

print(answer)
