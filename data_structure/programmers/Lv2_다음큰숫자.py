def solution(n):
    num = n
    while True:
        num += 1
        if format(num, "b").count("1") == format(n, "b").count("1"):
            return num
