def solution(friends, gifts):
    f_len, g_len = len(friends), len(gifts) # 친구 수, 선물 수

    adj = [[0] * f_len for _ in range(f_len)] # 친구 간 give and take 관계를 나타내는 인접 행렬
    result = [0] * f_len

    p_dic = { friend : 0 for friend in friends } # 선물 지수 계산
    f_key = { friend : index for index, friend in enumerate(friends) } # 인덱싱 (이름 : 순서)
    f_val = { index : friend for index, friend in enumerate(friends) } # 인덱싱 (순서 : 이름)

    # 선물 지수 계산
    for i in range(g_len):
        giver, taker = gifts[i].split(" ")
        p_dic[giver], p_dic[taker] = p_dic[giver]+1, p_dic[taker]-1
        adj[f_key[giver]][f_key[taker]] += 1

    for i in range(f_len-1):
        for j in range(i+1, f_len):
            if adj[i][j] == adj[j][i]: # give and take 선물 수가 같으면
                if p_dic[f_val.get(i)] > p_dic[f_val.get(j)]: # 선물 지수 비교
                    result[i] += 1
                elif p_dic[f_val.get(i)] < p_dic[f_val.get(j)]:
                    result[j] += 1
            else: # give and take 선물 수가 다르면
                if adj[i][j] > adj[j][i]:
                    result[i] += 1
                else:
                    result[j] += 1

    return max(result)
