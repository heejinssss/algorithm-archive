while True:
    word = input()
    stack = []
    if word == '.':
        break

    for word in word: # 단일어도 반복문 사용 가능
        if not stack: # 스택이 비어있을 때
            if word == '[' or word == '(' or word == ']' or word == ')':
                stack.append(word)
        elif word == '[' or word == '(': # 스택이 비어있지 않을 때 (입력 단어가 '[')
            stack.append(word)
        elif word == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                break
        elif word == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                break
        else: # 문자이거나 공백인 경우 pass
            continue

    if not stack:
        print('yes')
    else:
        print('no')