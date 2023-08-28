def future_city(n,m,l):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    for i in range(m):
        a, b = tuple(l[i])
        graph[a][b] = 1
        graph[b][a] = 1

    x, k = tuple(l[-1])

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    distance = graph[1][k] + graph[k][x]

    if distance >= 1e9:
        return -1
    else:
        return distance