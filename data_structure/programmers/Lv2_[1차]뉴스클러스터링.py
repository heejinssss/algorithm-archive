def solution(str1, str2):
    answer = 0

    arr1, arr2 = distribute(str1), distribute(str2)

    if not arr1 and not arr2:
        return 65536

    inter, union = [], []

    # 교집합, 합집합
    if len(arr1) < len(arr2):
        inter, union = makeSet(arr1, arr2)
    else:
        inter, union = makeSet(arr2, arr1)

    if len(union) == 0:
        return 65536

    return int(len(inter) / len(union) * 65536)

# 두 글자씩 끊어서 다중집합의 원소로 만드는 함수
def distribute(arr):
    result = []
    for i in range(len(arr)-1):
        if arr[i].isalpha() and arr[i+1].isalpha():
            result.append(arr[i:i+2].lower())
    return result

# 합집합, 교집합 만드는 함수
def makeSet(arr1, arr2):

    inter, union = [], []

    for a in arr1:
        if a in arr2:
            arr2.remove(a)
            inter.append(a)
        union.append(a)
    union.extend(arr2)
    
    return inter, union