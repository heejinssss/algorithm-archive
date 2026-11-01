# 다시 풀기

from collections import Counter

def solution(weights):
    answer = 0

    dic = { x : -1 for x in weights }
    counter = Counter(weights)
    result = []

    for i in range(len(weights)-1):
        wi = weights[i]
        tmp = 0
        # 기존에 탐색한 값과 동일한 무게이면
        if dic[wi] >= 0:
            continue
        for j in range(i+1, len(weights)):
            wj = weights[j]
            if [wi, wj] not in result and [wj, wi] not in result:
                if wi == wj or wi*2 == wj*3 or wi*2 == wj*4 or wi*3 == wj*2 or wi*3 == wj*4 or wi*4 == wj*2 or wi*4 == wj*3:            
                    result.append([wi, wj])
                    tmp += 1
        dic[wi] = tmp*counter[wi] if tmp else 0

    for value in dic.values():
        if value != -1:
            answer += value

    return answer
