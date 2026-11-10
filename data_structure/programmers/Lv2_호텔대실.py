# 다시 풀기

from collections import deque

def solution(book_time):
    answer = 0
    q = deque()

    # 예약 시간을 시작 시간을 기준으로 오름차순 정렬
    book_time.sort()

    for start, end in book_time:
        start = to_minutes(start)
        end = to_minutes(end) + 10

        if q and q[0] <= start:
            q.popleft()

        q.append(end)
        answer = max(answer, len(q))

    return answer

# 시간을 분 단위로 변환하는 함수
def to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m