def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        # 희망 출근 시간
        sh = schedules[i] // 100
        sm = schedules[i] % 100

        # +10분
        sm += 10
        if sm >= 60:
            sh += 1
            sm -= 60

        ok = True
        day = startday

        for j in range(7):
            th = timelogs[i][j] // 100
            tm = timelogs[i][j] % 100

            # 평일만 검사
            if 1 <= day <= 5:
                if th > sh or (th == sh and tm > sm):
                    ok = False
                    break

            day += 1
            if day == 8:
                day = 1

        if ok:
            answer += 1

    return answer