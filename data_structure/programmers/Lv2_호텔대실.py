# 다시 풀기

from collections import deque

def solution(book_time):

    answer = 0
    q = deque()

    for time in book_time:
        pass

    return answer

def to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m