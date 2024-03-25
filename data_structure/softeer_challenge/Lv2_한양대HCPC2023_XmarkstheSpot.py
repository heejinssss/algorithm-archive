import sys

T = int(sys.stdin.readline())
word_pair = [sys.stdin.readline().strip() for _ in range(T)]

# 테스트 케이스는 통과하지만 시간 초과 위험성
# T = int(sys.stdin.readline())
# word_pair = [input() for _ in range(T)]

result = [0] * T

for i in range(T):
    word = word_pair[i].upper() # 전체 대문자화
    indexX = word.index('X')
    result[i] = word[indexX+((len(word_pair[i])+1)//2)]

print(*result, sep="") # "+=" 연산은 시간 초과 위험성