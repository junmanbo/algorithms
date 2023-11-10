def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(n, computers, visited, start):
        stk = [start]

        while stk:
            x = stk.pop()
            if visited[x] is False:
                visited[x] = True

            for i in range(n):
                if computers[x][i] == 1 and visited[i] is False:
                    stk.append(i)

    i = 0
    while False in visited:
        if visited[i] is False:
            dfs(n, computers, visited, i)
            answer += 1
        i += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))
