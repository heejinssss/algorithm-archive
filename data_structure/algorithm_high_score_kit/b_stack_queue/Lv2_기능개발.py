def solution(progresses, speeds):
    answer = []

    waiting = 0
    deploy = 0

    while progresses != []:

        if progresses[0] + speeds[0] * waiting >= 100:
            deploy += 1
            progresses.pop(0)
            speeds.pop(0)

        else:
            waiting = (100 - progresses[0]) // speeds[0]

            if ((100 - progresses[0]) % speeds[0]) != 0:
                waiting += 1

            answer.append(deploy)
            deploy = 0
    
    answer.append(deploy)

    return answer[1:]