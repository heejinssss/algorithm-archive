from collections import Counter

def solution(want, number, discount):

    answer = 0

    want_dic = { w : cnt for w, cnt in zip(want, number) }
    _sum = sum(number)

    # 남은 일자 모두 구매해도 number의 합계보다 작은 경우 제외
    if len(discount) < _sum:
        return 0

    # discount 리스트에 특정 또는 전체 want 항목이 없는 경우 제외
    for w in want:
        if w not in discount:
            return 0

    for i in range(len(discount)-9):

        arr = discount[i:i+10]
        counter = Counter(arr)

        # 현재~10일 안에 want 항목을 모두 구매할 수 있는 경우를 반복 점검
        for w in want:
            if w not in arr or want_dic[w] > counter[w]:
                break
        else:
            answer += 1

    return answer
