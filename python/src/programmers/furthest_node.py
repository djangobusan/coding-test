from collections import deque


def furthest_node(n, edge):
    result = 0
    route = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    queue = deque()

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue.append(1)
    route[1] = 1

    # 계산

    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if route[g] == 0:
                queue.append(g)
                route[g] = route[now] + 1
    
    max_edge = max(route)

    for r in route:
        if r == max_edge:
            result = result + 1

    return result
