def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            left, right = 0, 0

            if 0 <= j-1:
                left = triangle[i-1][j-1]

            if j < len(triangle[i-1]):
                right = triangle[i-1][j]

            triangle[i][j] += max(left, right)

    return max(triangle[-1])