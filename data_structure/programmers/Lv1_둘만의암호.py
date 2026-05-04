def solution(s, skip, index):
    answer = ""
    new_alphabet = ""

    for i in range(97, 123):
        if chr(i) not in skip:
            new_alphabet += chr(i)

    for a in s:
        answer += new_alphabet[(new_alphabet.index(a)+index)%len(new_alphabet)]

    return answer

    # ord("a") : 97
    # ord("z") : 122
