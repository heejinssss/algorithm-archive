def solution(clothes):
    clothes.sort(key=lambda x : x[1])

    kindof = { clothes[0][1] : 1 }
    
    # 종류(key) & 개수(value)
    for i in range(0, len(clothes)-1):
        if clothes[i][1] == clothes[i+1][1]:
            kindof[clothes[i+1][1]] += 1
        else:
            kindof[clothes[i+1][1]] = 1
    
    total = 1
    values = list(kindof.values())
    for value in values:
        value += 1
        total *= value
        
    return total-1