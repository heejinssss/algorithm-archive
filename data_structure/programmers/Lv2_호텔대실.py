# 다시 풀기

# from collections import deque
import heapq

def solution(book_time):
    answer = 0
    # q = deque()
    q = []

    book_time.sort()

    for start, end in book_time:
        start = to_minutes(start)
        end = to_minutes(end) + 10

        # if q and q[0] <= start:
        #     q.popleft()

        # q.append(end)
        # answer = max(answer, len(q))
    
        if q and q[0] <= start:
            heapq.heappop(q)

        heapq.heappush(q, end)
        answer = max(answer, len(q))

    return answer

def to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m
