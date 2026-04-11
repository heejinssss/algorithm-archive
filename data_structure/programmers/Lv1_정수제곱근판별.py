import math

def solution(n):
    num = math.sqrt(n)

    if int(num) == num:
        return (num + 1) ** 2
    else:
        return -1