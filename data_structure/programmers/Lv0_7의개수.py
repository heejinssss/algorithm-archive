def solution(array):
    answer = 0
    
    """
    for num in array:
        for str_n in str(num):
            if (str_n == "7"):
                answer += 1

    return answer
    """

    return str(array).count("7")
