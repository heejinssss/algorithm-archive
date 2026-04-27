def solution(players, callings):

    pos = { player: i for i, player in enumerate(players) }

    for calling in callings:

        cur = pos[calling]
        
        pre_player = players[cur - 1]
        
        players[cur - 1], players[cur] = players[cur], players[cur - 1]
        
        pos[calling] = cur - 1

        pos[pre_player] = cur
    
    return players
