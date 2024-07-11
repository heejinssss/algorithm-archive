import math

def solution(brown, yellow):
    answer = []

    for c in range(1, int(math.sqrt(yellow))+1):
        if yellow % c == 0:
            outer = (c+2) * (yellow//c+2)
            if outer-yellow == brown:
                answer = [max(c+2, yellow//c+2), min(c+2, yellow//c+2)]

    return answer