import math

def solution(n, k):
    answer = 0
    
    kNum = ""

    while n > 0:
        n, mod = divmod(n, k)
        kNum += str(mod)

    kNum = kNum[::-1]

    arr = kNum.split("0")

    for a in arr:
        if a and a != "1" and isPrime(int(a)):
            answer += 1

    return answer

def isPrime(n):
    cnt = 0

    for i in range (2, int(math.sqrt(n)+1)):
        if n % i == 0:
            cnt += 1

    return False if cnt else True
