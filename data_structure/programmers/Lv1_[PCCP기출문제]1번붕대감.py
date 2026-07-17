def solution(bandage, health, attacks):
    """
    bandage: 붕대 감기 기술의 시전 시간, 1초당 회복량, 추가 회복량
    health: 최대 체력
    attacks: 몬스터의 공격 시간과 피해량
    """

	# 체력, 연속 시간, 공격 시간, 공격력, 현재 시간
    blood, cnt, now, time, damage = health, 0, 0, 0, 0

    for attack in attacks:

        if blood <= 0:
            return -1

        time, damage = attack

        while now < time:

            now += 1
            cnt += 1

            if blood == health: # 이미 최대 체력이면
                continue

            # 최대 체력이 아니라면
            if blood + bandage[1] <= health: 
                blood += bandage[1]
            else:
                blood = health

            # 연속 기술 사용에 성공했다면
            if cnt == bandage[0]:
                if blood + bandage[2] <= health:
                    blood += bandage[2]
                else:
                    blood = health
                cnt = 0

        blood -= damage
        cnt = 0
        now += 1

    return blood if blood > 0 else -1
