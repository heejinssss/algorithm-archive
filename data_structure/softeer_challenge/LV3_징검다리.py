# 최장 증가 부분 수열(LIS, Longest Increasing Subsequence)
import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))

length = [1] * n
for i in range(n):
    for j in range(i):
        if heights[j] < heights[i]:
            length[i] = max(length[i], length[j]+1)

print(max(length))