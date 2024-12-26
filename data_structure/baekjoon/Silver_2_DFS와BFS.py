# import heapq
from collections import deque

N, M, V = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)
    # heapq.heappush(adj[i], j)
    # heapq.heappush(adj[j], i)

for i in range(1, N+1):
    adj[i].sort()

dfs_result = []
bfs_result = []

def dfs(n):
    dfs_result.append(n)
    visited[n] = 1

    for m in adj[n]:
        if visited[m] != 1:
            dfs(m)

def bfs(n):
    q = deque([])

    q.append(n)
    bfs_result.append(n)
    visited[n] = 1

    while q:
        s = q.popleft()
        for m in adj[s]:
            if visited[m] != 1:
                q.append(m)
                bfs_result.append(m)
                visited[m] = 1        
    
visited = [0] * (N+1)
dfs(V)

visited = [0] * (N+1)
bfs(V)

print(*dfs_result)
print(*bfs_result)