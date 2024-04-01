def solution(array, commands):
    answer = [0] * len(commands)
    idx = 0

    for command in commands:
        tmp = [0] * (1+abs(command[1]-command[0])) # i~j번째 원소 담을 배열 선언
        n = 0 # i~j번째 원소를 담기 위해 index 값 1씩 증가
        for k in range(command[0]-1, command[1]):
            tmp[n] = array[k]
            n += 1
        tmp.sort()
        answer[idx] = tmp[command[2]-1]
        idx += 1
    
    while 0 in answer:
        answer.remove(0)
    return answer