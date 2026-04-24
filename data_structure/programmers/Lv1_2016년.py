def solution(a, b):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dows = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    count = 0

    for i in range(1, len(days)):
        if i == a:
            count += b
            break
        count += days[i]

    return dows[count%7-1]
