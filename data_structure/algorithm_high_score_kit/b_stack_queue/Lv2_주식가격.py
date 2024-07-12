# 시간 복잡도 개선 필요
def solution(prices):
    answer = []
    
    N = len(prices)
    stack = [0]*N
    
    for cur in range(N-1):
        cnt = 0
        currentPrice = prices[cur]
        for nexxt in range(cur+1, N):
            if currentPrice > prices[nexxt]:
                stack[cur] += 1
                break
            cnt += 1
        stack[cur] += cnt
    
    answer = stack

    return answer[:-1] + [0]