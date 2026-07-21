def solution(s):

    a1, a2 = 0, 0

    while True:
        count_0 = s.count("0")
        a2, c, c_bin = a2 + count_0, len(s) - count_0, "" # 제거한 0의 개수, 제거한 0의 개수 2진수 표현

        while c > 0:
            div, mod = c//2, c%2
            c, c_bin = div, str(mod) + c_bin

        a1 += 1
        s = c_bin

        if s == "1":
            return [a1, a2]
