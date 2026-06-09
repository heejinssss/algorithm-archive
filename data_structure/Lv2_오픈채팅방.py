def solution(record):
    answer = []

    fin_nickname = {}

    for r in record:
        if r[0] != "L":
            fin_nickname[r.split(" ")[1]] = r.split(" ")[2]

    for r in record:
        # 닉네임 변경은 알림 불필요
        if r[0] == "E":
            answer.append(fin_nickname[r.split(" ")[1]]+"님이 들어왔습니다.")
        elif r[0] == "L":
            answer.append(fin_nickname[r.split(" ")[1]]+"님이 나갔습니다.")

    return answer
