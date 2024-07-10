from collections import defaultdict, deque

def bfs(graph, startPoint):
    visited = [startPoint]
    q = deque([startPoint])
    cnt = 1

    while q:
        node = q.popleft()
        
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                q.append(adj)
                cnt += 1
    return cnt

def solution(n, wires):
    answer = 0
    
    case = []
    
    for wire1 in wires:
        graph = defaultdict(list)
        sx, sy = wire1
        
        for wire2 in wires:
            if wire1 == wire2:
                continue
            nx, ny = wire2
            graph[nx].append(ny)
            graph[ny].append(nx)
        
        n1 = bfs(graph, sx)
        n2 = bfs(graph, sy)
        case.append(abs(n1-n2))
    
    answer = min(case)

    return answer