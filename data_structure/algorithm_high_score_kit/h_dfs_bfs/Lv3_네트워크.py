from collections import deque

def solution(n, computers):
    
    q = deque([])
    v = [[0] * n for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and v[i][j] == 0:
                # 두 컴퓨터가 연결되어 있고, 첫 방문이라면
                q.append([i,j]) # 연결된 두 컴퓨터 번호 append
                while q:
                    x, y = q.popleft() # 연결된 두 컴퓨터 번호 출력
                    for k in range(n): # i(x에 대입)번째(고정) 컴퓨터와 k번째 컴퓨터 비교              
                        if v[x][k] == 0 and computers[x][k] == 1: # 두 컴퓨터가 연결되어 있고, 첫 방문이라면
                            v[x][k] = 1
                            q.append([k,x]) # 다음 컴퓨터 비교
                answer += 1

    return answer