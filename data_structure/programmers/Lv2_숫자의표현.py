def solution(n):
    answer = 0
	
    for i in range(1, n+1):
        start = 0
        while True:
            if start < n:
                start += i
                i += 1
            elif start > n:
                break
            else:
                answer += 1
                break
    return answer
