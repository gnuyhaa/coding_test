def solution(n, computers):
    answer = 0
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                arr[i].append(j)
                arr[j].append(i)
    visited = []
    def dfs(v,visited,arr):
        if v not in visited:
            visited.append(v)
        for i in arr[v]:
            if i not in visited:
                visited = dfs(i,visited,arr)
        return visited
    count = 0
    for i in range(n):
        if i not in visited:
            visited = dfs(i,visited,arr)
            count+=1

    return count
