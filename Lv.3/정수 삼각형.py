def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j==i: # 오른쪽 위가 없음
                triangle[i][j] += triangle[i-1][j-1]
            elif j==0: #왼쪽 위가 없음
                triangle[i][j] += triangle[i-1][j]
            else: # 왼쪽 오른쪽 둘다 있음
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])
