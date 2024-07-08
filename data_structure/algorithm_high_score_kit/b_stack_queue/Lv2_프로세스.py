def solution(priorities, location):

    T = answer = len(priorities) # 확인하고 싶은 프로세스의 우선순위가 가장 낮다는 전제로 시작
    turn = [i for i in range(T)]

    while len(priorities) > 1:
        p = priorities.pop(0)
        t = turn.pop(0)

        # 큐에 대기 중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면
        if p < max(priorities):
            priorities.append(p)
            turn.append(t)
        # 큐에 대기 중인 프로세스 중 우선순위가 더 높은 프로세스가 없다면
        else:
            # 현재 실행 중인 프로세스와 확인하고 싶은 프로세스가 같다면
            if t == location:
                answer = T - len(turn)
                break

    return answer