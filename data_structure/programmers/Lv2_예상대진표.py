def cal(num):
    return (num + (1 ** (num % 2))) // 2

def solution(n,a,b):

    answer = 0

    while (True):

        answer += 1

        if (a - (-1)**(a % 2) == b): # a가 홀수이든 짝수이든 b와 대결한다면
            return answer

        a, b = cal(a), cal(b)
