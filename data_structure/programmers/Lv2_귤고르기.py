from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    count = sorted(count.items(), key=lambda pair:pair[1], reverse=True)

    arr = []
    for key, value in count:
        while value > 0:
            arr.append(key)
            value -= 1
            if len(arr) == k:
                return len(set(arr))
