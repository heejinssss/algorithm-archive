# 다시 풀기

def solution(weights):
    answer = 0

    for i in range(len(weights)):
        wi = weights[i]
        for j in range(i+1, len(weights)):
            wj = weights[j]
            if wi == wj or wi*2 == wj*3 or wi*2 == wj*4 or wi*3 == wj*2 or wi*3 == wj*4 or wi*4 == wj*2 or wi*4 == wj*3:
                answer += 1

    return answer
