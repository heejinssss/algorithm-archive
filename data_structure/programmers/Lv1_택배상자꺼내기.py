def solution(n, w, num):
	
    cnt = 1

    while True:
        if num % w == 0: # n이 w의 배수이면, 바로 위 숫자는 cur+1
            num += 1
        else: # n이 w의 배수가 아니면, 바로 위 숫자는 (w*2*((num//w)+1))+1-num
            num = (w*2*((num//w)+1))+1-num

        if num > n:
            return cnt
        else:
            cnt += 1
