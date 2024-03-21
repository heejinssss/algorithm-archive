def solution(genres, plays):
    answer = []

    music_list = []
    music_dict = {}

    for i in range(0, len(genres)):
        music_list += [[genres[i], plays[i], i]] # 장르, 재생 횟수, 고유번호
        # 이전에 기록한 장르이면
        if genres[i] in music_dict:
            music_dict[genres[i]] += plays[i]
        # 처음으로 기록되는 장르이면
        else:
            music_dict[genres[i]] = plays[i]
    
    music_list.sort(key=lambda x : (x[0], -x[1], x[2])) # [장르, 재생 횟수, 고유번호]
    bestplaytime = sorted(music_dict.items(), key=lambda x : x[1], reverse=True)

    # for i, key in enumerate(bestplaytime.values()):
    # for i, key in enumerate(bestplaytime.keys()):
    for genres in bestplaytime:
        temp = []
        for music in music_list:
            if (genres[0] == music[0]) and (len(temp) < 2):
                temp += [music[2]]
        answer += temp

    return answer