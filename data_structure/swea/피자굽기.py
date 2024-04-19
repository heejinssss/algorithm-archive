T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split())) # 화덕 크기, 피자 개수
    C = list(map(int, input().split())) # 피자 치즈 현황
    q = []

    for i in range(0, N):
        q.append([i+1, C.pop(0)])

    idx = N
    while len(q) > 1:
        pizza = q.pop(0) # pizza = [i번째, 남은 치즈 양]
        if pizza[1]//2 > 0: # 피자의 치즈가 다 녹지 않았다면
            q.append([pizza[0], pizza[1]//2]) # 뒷 순서로 다시 넣기
        else: 
            if C: # 아직 화덕에 넣지 못한 피자가 있다면
                idx += 1
                q.append([idx, C.pop(0)])

    print(f'#{test_case} {q[0][0]}')