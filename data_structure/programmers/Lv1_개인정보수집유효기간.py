def solution(today, terms, privacies):
    answer = []

    dic = { kind[0] : int(kind[2:]) for index, kind in enumerate(terms) }

    ty, tm, td = map(int, today.split("."))

    for i in range(len(privacies)):
        date, kind = privacies[i].split() # ["2021.05.02", "A"]
        sy, sm, sd = map(int, date.split(".")) # [2021, 5, 2]
        sy = sy + ((sm + dic[kind] - 1) // 12)
        sm = (sm + dic[kind]) % 12 if (sm + dic[kind]) % 12 else 12

        t_str = f"{ty:04d}{tm:02d}{td:02d}"
        s_str = f"{sy:04d}{sm:02d}{sd:02d}"

        if int(t_str) >= int(s_str):
            answer.append(i + 1)

    return answer
