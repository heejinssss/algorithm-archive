"""
빵 : 1, 야채 : 2, 고기 : 3
"""

def solution(ingredient):
    answer = 0
    
    stack = []

    for i in ingredient:
        stack.append(i)

        if len(stack) >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                answer += 1

                for _ in range(4):
                    stack.pop()

    return answer
