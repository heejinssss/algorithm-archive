def solution(skill, skill_trees):
    answer = 0

    dic = {s: i for i, s in enumerate(skill)}

    for skill_tree in skill_trees:
        str = [s for s in skill_tree if s in dic]

        # 스킬 트리에서 선행 스킬이 없는 경우
        if len(str) == 0:
            answer += 1
            continue

        if dic[str[0]] == 0:
            for i in range(len(str)-1):
                # 현재 단계 바로 직전 선행 단계가 아닌 경우 반복 중단
                if dic[str[i]] < dic[str[i+1]] - 1:
                    break
            else:
                answer += 1

    return answer
