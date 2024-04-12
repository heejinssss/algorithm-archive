def solution(citations):

    citations.sort()
    
    n = len(citations)
    
    maxV = n
    
    for i in range(n - 1, -1, -1):
        h = citations[i] # h의 최대값을 현재까지의 최고 원소로 고정
        if (h <= n-i) and (i <= h): # 현재까지의 원소 중 최댓값이 있다면
            maxV = h
            return maxV
        else: # 현재까지의 원소 중 최댓값이 없다면
            pivot = h
            while (pivot > citations[i-1]):
                if (pivot-1 <= n-i) and (i <= pivot-1):
                    return pivot-1
                pivot -= 1
        continue
    
    return maxV