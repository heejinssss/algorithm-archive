# 다시 풀기

def solution(book_time):
    answer = 0

    bt = sorted(book_time, key=lambda x: (int(x[0][0:2]), int(x[0][3:5]), int(x[1][0:2]), int(x[1][3:5])))

    print(bt)

    room = [ [] for _ in range(len(book_time)) ]

    for time in book_time:
        pass

    return answer