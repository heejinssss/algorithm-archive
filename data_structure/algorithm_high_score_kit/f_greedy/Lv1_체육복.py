def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 옷을 가져온 학생 중, 도난당하지 않은 학생
    rly_reserve = [x for x in reserve if x not in lost]
    rly_reserve.sort()
    
    # 도난당한 학생 중, 여벌 옷도 없는 학생
    rly_lost = [x for x in lost if x not in reserve]
    rly_lost.sort()
    
    for can_reserve in rly_reserve:
        if can_reserve-1 in rly_lost:
            rly_lost.remove(can_reserve-1)
        elif can_reserve+1 in rly_lost:
            rly_lost.remove(can_reserve+1)

    answer = n-len(rly_lost)

    return answer