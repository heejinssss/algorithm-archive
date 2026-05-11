def solution(s):
    answer = ""
    
    s_list = s.split(" ")

    for word in s_list:
        for i in range(len(word)):
            answer += word[i].lower() if i%2 else word[i].upper()
        answer = answer + " "

    return answer[:len(answer)-1]
