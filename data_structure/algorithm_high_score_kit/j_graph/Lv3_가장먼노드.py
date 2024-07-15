from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = {i:[] for i in range(n+1)}
    distance = [0]*(n+1)
    q = deque([])
    q.append(1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    while q:
        now = q.popleft()
        
        for nexxt in graph[now]:
            if distance[nexxt] == 0:
                distance[nexxt] = distance[now]+1
                q.append(nexxt)
    
    return distance[2:].count(max(distance[2:]))

""" Time Out (list vs dictionary)
from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[0]*(n+1) for _ in range(n+1)]
    distance = [0]*(n+1)
    q = deque([])
    q.append(1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    while q:
        now = q.popleft()
        
        for nexxt in graph[now]:
            if distance[nexxt] == 0:
                distance[nexxt] = distance[now]+1
                q.append(nexxt)
    
    return distance[2:].count(max(distance[2:]))
"""