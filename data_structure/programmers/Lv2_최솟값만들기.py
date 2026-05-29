def solution(A,B):
    answer = 0

    aArr = sorted(A)
    bArr = sorted(B, reverse=True)

    for a, b in zip(aArr, bArr):
        answer += a*b

    return answer
