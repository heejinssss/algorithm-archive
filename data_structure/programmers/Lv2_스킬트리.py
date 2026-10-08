def solution(skill, skill_trees):
    answer = 0

    dic = {s: i for i, s in enumerate(skill)}

    for skill_tree in skill_trees:
        str = [s for s in skill_tree if s in dic]
        
        for i in range(len(str)-1):
            if dic[str[i]] > dic[str[i+1]]:
                break
        else:
            answer += 1

    return answerstatus