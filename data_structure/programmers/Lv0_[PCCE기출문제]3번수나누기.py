number = int(input())

answer = 0

for i in range(len(str(number))//2): # 수정 전 : for i in range(1)
    answer += number % 100
    number //= 100

print(answer)
