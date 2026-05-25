def solution(s, n):
    answer = ''

    for word in s:
        if 97 <= ord(word) <= 122:
            word = chr(ord(word)+n-26) if ord(word)+n > 122 else chr(ord(word)+n)
        if 65 <= ord(word) <= 90:
            word = chr(ord(word)+n-26) if ord(word)+n > 90 else chr(ord(word)+n)
        answer += word

    # a 97, z 122, A 65, Z 90
    
    return answer
