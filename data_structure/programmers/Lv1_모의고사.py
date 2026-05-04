def solution(answers):
    answer = []
    
    f1 = [1, 2, 3, 4, 5] # max: 4
    f2 = [2, 1, 2, 3, 2, 4, 2, 5] # max: 7
    f3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # max : 9
    a, b, c = 0, 0, 0

    for i in range(len(answers)):
        a = a + 1 if f1[i%5]  == answers[i] else a
        b = b + 1 if f2[i%8]  == answers[i] else b
        c = c + 1 if f3[i%10] == answers[i] else c

    if a > b:
        max_value = a
    else:
        max_value = b

    if max_value < c:
        max_value = c

    for i in range(1, 4):
        if max_value == [a, b, c][i-1]:
            answer.append(i)

    return answer
