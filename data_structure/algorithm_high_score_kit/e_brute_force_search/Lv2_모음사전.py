def solution(word):
    word_list = list(word) # 문자열 -> 원소로 분리

    number = [[1, 782, 1563, 2344, 3125], # A____
              [1, 157, 313, 469, 625],    # _A___
              [1, 32, 63, 94, 125],       # __A__
              [1, 7, 13, 19, 25],         # ___A_
              [1, 2, 3, 4, 5]]            # ____A

    index = 0
    for i in range(0, len(word_list)):
        if word_list[i] == 'A':
            index += number[i][0]
        elif word_list[i] == 'E':
            index += number[i][1]
        elif word_list[i] == 'I':
            index += number[i][2]
        elif word_list[i] == 'O':
            index += number[i][3]
        elif word_list[i] == 'U':
            index += number[i][4]        

    return index