# 다시 풀기

def solution(weights):
    answer = 0

    dic = { x : -1 for x in weights }

    for i in range(len(weights)):
        wi = weights[i]
        tmp = 0
        if dic[wi] >= 0:
            continue
        for j in range(i+1, len(weights)):
            wj = weights[j]
            if wi == wj or wi*2 == wj*3 or wi*2 == wj*4 or wi*3 == wj*2 or wi*3 == wj*4 or wi*4 == wj*2 or wi*4 == wj*3:
                tmp += 1
        dic[wi] = tmp if tmp else 0

    answer = sum(dic.values())

    return answer