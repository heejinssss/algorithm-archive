def solution(id_list, report, k):

    pos = { id : index for index, id in enumerate(id_list) }
    ban = [0] * len(id_list)
    ans = [0] * len(id_list)

    for r in list(set(report)):
        r_list = r.split(" ")
        ban[pos[r_list[1]]] += 1

    for r in list(set(report)):
        r_list = r.split(" ")
        if ban[pos[r_list[1]]] >= k:
            ans[pos[r_list[0]]] += 1

    return ans