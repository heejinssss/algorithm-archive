"""
# 교집합
print(set1 & set2)
print(set1.intersection(set2))

# 합집합
print(set1 | set2)
print(set1.union(set2))

# 차집합
print(set1 - set2)
print(set1.difference(set2))
"""

def solution(s):
    answer = []

    tmp = sorted(s[2:len(s)-2].split("},{"), key=lambda x : len(x))
    arr = []

    for t in tmp:
        lst = t.split(",")
        arr.append(lst)

    answer.append(int(arr[0][0]))

    for i in range(len(arr)-1):
        set1, set2 = set(arr[i]), set(arr[i+1])
        answer.append(int(list(set2-set1)[0]))

    return answer
