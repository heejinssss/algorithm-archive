def solution(s):

    first_word = s[0]
    x_num = 1 # 시작 글자 개수
    o_num = 0 # 시작 글자와 다른 글자 개수
    w_num = 0 # 분리된 단어 개수

    for i in range(1, len(s)):

        if not x_num and not o_num:
            first_word = s[i]

        if first_word == s[i]:
            x_num += 1
        else:
            o_num += 1

        if x_num == o_num:
            x_num, o_num, w_num = 0, 0, w_num+1

    return w_num if x_num == o_num else w_num+1
