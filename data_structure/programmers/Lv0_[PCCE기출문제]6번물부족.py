def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = usage * (100 + change[i]) / 100 # 수정 전 : usage = total_usage * change[i]/10
        total_usage += usage
        if total_usage > storage:
            return i

    return -1