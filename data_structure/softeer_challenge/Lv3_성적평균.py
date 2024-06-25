import sys

# sys.stdin.readline()
n, k = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))
scope = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

for i in range(k):
    start = scope[i][0] - 1
    end = scope[i][1]
    total = end-start
    avg = sum(scores[start:end])/total
    result = format(round(avg, 2), ".2f") # 공백 0으로 채우기
    print(result)