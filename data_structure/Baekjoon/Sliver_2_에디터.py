import sys
from collections import deque

stackL = deque(list(map(str, input())))
stackR = deque([])
n = int(input())

# 초기 단어
edit = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

for e in edit:
    if e[0] == 'L':
        if stackL: # 커서가 문장의 맨 앞이 아니면
            stackR.appendleft(stackL.pop()) # 커서 바로 앞 문자를 커서 바로 뒤로 옮김
    elif e[0] == 'D':
        if stackR: # 커서가 문장의 맨 뒤가 아니면
            stackL.append(stackR.popleft()) # 커서 바로 뒤 문자를 커서 바로 앞으로 옮김
    elif e[0] == 'B':
        if stackL: # 커서가 문장의 맨 앞이 아니면
            stackL.pop() # 커서 바로 앞 문자 삭제
    elif e[0] == 'P':
        stackL.append(e[1])

print("".join(stackL+stackR))