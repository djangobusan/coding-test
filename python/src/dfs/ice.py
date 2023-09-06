n = 0
m = 0
graph = []


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


def ice(adj_matrix):
    global n, m, graph
    n = len(adj_matrix)
    m = len(adj_matrix[0])
    graph = adj_matrix
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    return result
