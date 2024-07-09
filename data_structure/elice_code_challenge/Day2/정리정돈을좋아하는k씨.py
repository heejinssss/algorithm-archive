import heapq

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
mList = [list(map(int, input().split())) for _ in range(M)]

for scope in mList:
    hq = []
    result = []
    start = scope[0] - 1
    end = scope[1]
    target = scope[-1] - 1
    for i in range(start, end):
        heapq.heappush(hq, numbers[i])
    
    for j in range(len(hq)):
        heapq.heappush(result, heapq.heappop(hq))
    
    print(result[target])
