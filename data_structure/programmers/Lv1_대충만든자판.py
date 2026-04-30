def solution(keymap, targets):

    dic_list = []

    for key in keymap:
        dic_list.append({ k: key.index(k)+1 for i, k in enumerate(key) })

    for target in targets:
        cnt = 0

        for t in target:
            val = 100

            for dic in dic_list: # {"A":0,"B":1,"C":3,"D":4}
                if t in list(dic.keys()):
                    val = min(dic[t], val)

            if val == 100:
                cnt = -1
                break
            else:
                cnt += val

        answer.append(cnt)

    return answer
