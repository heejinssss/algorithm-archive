def cal(newList, ability):
    supervisor = 0
    for n in newList:
        a = n // ability
        if (n % ability != 0):
            supervisor += a + 1
        else:
            supervisor += a

    return supervisor

n = int(input())
students = list(map(int, input().split()))
main, sub = map(int, input().split())

stack = []
cnt = 0
for student in students:
    cnt += 1
    if (student-main) > 0:
        stack.append(student-main)
b = cal(stack, sub)

print(cnt + b)