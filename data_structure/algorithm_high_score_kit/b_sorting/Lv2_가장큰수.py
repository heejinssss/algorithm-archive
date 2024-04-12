def solution(numbers):
        
    lst = list(map(str, numbers))
    
    order = sorted(lst, key=lambda x: x * 3, reverse=True)

    if order[0] == "0":
        return "0"

    answer = ''.join(order)
    
    return answer