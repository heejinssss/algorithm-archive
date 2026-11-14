import heapq

def solution(book_time):
    answer = 0
    q = []

    book_time.sort()

    for start, end in book_time:
        start = to_minutes(start)
        end = to_minutes(end) + 10

        if q and q[0] <= start:
            heapq.heappop(q)

        heapq.heappush(q, end)
        answer = max(answer, len(q))

    return answer

# 분으로 변환하는 함수
def to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m