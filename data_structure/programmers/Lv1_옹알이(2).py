def solution(babbling):
    answer = 0
    can = ["aya", "woo", "ma", "ye"]

    for b in babbling:
        for c in can:
            if c*2 not in b:
                b = b.replace(c, " ")
        answer = answer + 1 if b.strip() == "" else answer

    return answer