def solution(lines):
    answer = 0

    arr = [0] * 201

    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            if max(lines[i][0], lines[j][0]) < min(lines[i][1], lines[j][1]):
                for k in range(max(lines[i][0], lines[j][0]), min(lines[i][1], lines[j][1])):
                    arr[k + 100] = 1

    return arr.count(1)
