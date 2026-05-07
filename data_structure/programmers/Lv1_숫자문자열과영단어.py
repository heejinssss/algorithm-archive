def solution(s):
    answer = s

    dic = { "zero"  : "0",
            "one"   : "1",
            "two"   : "2",
            "three" : "3",
            "four"  : "4",
            "five"  : "5",
            "six"   : "6",
            "seven" : "7",
            "eight" : "8",
            "nine"  : "9" }

    for key, value in dic.items():
        answer = answer.replace(key, value)

    """
    answer = ""

    dic = { "zero"  : "0",
            "one"   : "1",
            "two"   : "2",
            "three" : "3",
            "four"  : "4",
            "five"  : "5",
            "six"   : "6",
            "seven" : "7",
            "eight" : "8",
            "nine"  : "9" }

    sx = 0

    keyList, valueList = list(dic.keys()), list(dic.values())

    for i in range(1, len(s)+1):
        if s[sx:i] in keyList: # 알파벳이면
            answer = answer + dic[s[sx:i]]
            sx = i
        elif s[sx:i] in valueList: # 숫자이면
            answer = answer + s[sx:i]
            sx = i

    """

    return int(answer)