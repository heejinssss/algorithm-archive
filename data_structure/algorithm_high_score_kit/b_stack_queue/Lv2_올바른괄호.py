def solution(s):
    
    sList = list(map(str, s))

    stack = []
    
    for word in sList:
        if word == "(":
            stack.append(word)
        else:
            if not stack:
                return False
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
                
    return stack == []