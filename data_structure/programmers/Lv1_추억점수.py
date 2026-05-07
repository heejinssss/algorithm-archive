def solution(name, yearning, photo):
    answer = []
    
    dic = { n: y for n, y in zip(name, yearning)}

    for i in range(len(photo)):
        cnt = 0
        for j in range(len(photo[i])):
            if photo[i][j] in list(dic.keys()):
                cnt += dic[photo[i][j]]
        answer.append(cnt)

    return answer