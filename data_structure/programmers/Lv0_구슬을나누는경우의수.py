import math

def solution(balls, share):
    return math.comb(balls, share)

"""
def solution(balls, share):
    return f(balls) / (f(balls-share) * f(share))

def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)
"""
