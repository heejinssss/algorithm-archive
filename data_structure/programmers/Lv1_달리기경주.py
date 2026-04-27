def solution(players, callings):

    # 리스트에서 index()로 위치 찾으면 O(n)
    # 딕셔너리에서 key로 위치 조회하면 평균 O(1)
    pos = { player: i for i, player in enumerate(players) }

    for calling in callings:

        cur = pos[calling]
        
        pre_player = players[cur - 1]
        
        players[cur - 1], players[cur] = players[cur], players[cur - 1]
        
        pos[calling] = cur - 1

        pos[pre_player] = cur
    
    return players
