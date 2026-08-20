# 다시 풀기

from math import gcd
from functools import reduce

def solution(signals):

    def lcm(a, b):
        return a * b // gcd(a, b)

    def is_yellow(time, signal):
        g, y, r = signal
        period = g + y + r
        position = (time - 1) % period
        return g < position <= g + y

    # 모든 주기의 LCM 계산
    periods = [sum(signal) for signal in signals]
    max_time = reduce(lcm, periods)

    # LCM까지 범위에서 모든 신호등이 노란불인 시간 찾기
    for time in range(1, max_time + 1):
        if all(is_yellow(time, signal) for signal in signals):
            return time - 1

    return -1
