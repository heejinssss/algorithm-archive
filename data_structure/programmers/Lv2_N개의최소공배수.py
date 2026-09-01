def gcd(a, b):
    """최대공약수"""
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a

def lcm(a, b):
    """두 수의 최소공배수"""
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)

def solution(arr):
    """여러 수의 최소공배수"""
    result = 1

    for a in arr:
        result = lcm(result, a)

    return result
