import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
obj = []

for i in range(n):
    obj.append([i+1, lst[i]])

flag = False
while len(obj) > 1:
    done = [False] * n
    idx = 0
    while False in done and idx < len(obj)-1:
        if obj[idx][1] < obj[idx+1][1] and done[idx+1] == False:
            obj[idx+1][1] = obj[idx][1] + obj[idx+1][1]
            obj.remove(obj[idx])

            if len(obj) == 2:
                flag = True
                break

            done[obj[idx+1][0]-1] = 1
            done[obj[idx][0]-1] = 1
        elif obj[idx][1] >= obj[idx+1][1] and done[idx] == False:
            obj[idx][1] = obj[idx][1] + obj[idx+1][1]
            obj.remove(obj[idx+1])

            if len(obj) == 2:
                flag = True
                break

            done[obj[idx+1][0]-1] = 1
            done[obj[idx][0]-1] = 1
        else:
            idx += 1
    print(obj)
    print(obj[0][1]+obj[-1][1])
    print(obj[-1][0])
    break