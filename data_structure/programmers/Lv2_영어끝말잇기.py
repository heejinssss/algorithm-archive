def solution(n, words):
    comp = [words[0]]

    for i in range(1, len(words)):
        if words[i] in comp or comp[-1][-1] != words[i][0]:
            # 끝말잇기 규칙을 어긴 경우
            return [(i+1)%n if (i+1)%n else n,(i//n)+1]
        comp.append(words[i])

    else:
        return [0,0]
