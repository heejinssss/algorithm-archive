import sys
import heapq
input = sys.stdin.readline

lecture = []
n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(lecture, (e, s)) # "강의 종료 시간"을 기준으로 정렬되도록 값 삽입

now = 0
maxLecture = 0
while lecture:
    e, s = heapq.heappop(lecture) # 종료, 시작
    if s >= now: # 만약 해당 강의의 시작 시간이 앞선 강의의 종료 시간보다 크거나 같다면
        now = e
        maxLecture += 1 # 중복 강의실 배치 가능

print(maxLecture)