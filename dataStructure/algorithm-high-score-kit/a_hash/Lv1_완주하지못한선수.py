def solution(participant, completion):
    answer = ''
    par_dict = {}
    com_dict = {}

    for par in participant:
        if par in par_dict:
            par_dict[par] = par_dict[par] + 1
        else:
            par_dict[par] = 1
    
    for com in completion:
        if com in com_dict:
            com_dict[com] = com_dict[com] + 1
        else:
            com_dict[com] = 1

    for par in participant:
        if (par not in com_dict) or (par_dict[par] != com_dict[par]):
            answer = par

    return answer