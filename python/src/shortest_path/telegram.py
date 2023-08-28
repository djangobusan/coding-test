import heapq

def telegram(n,m,s,l):
    INF = int(1e9)    
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in range(m):
        x, y, z = tuple(l[i])
        graph[x].append((y, z))

    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    count = 0
    max_distance = 0
    for d in distance:
        if d != 1e9:
            count += 1
            max_distance = max(max_distance, d)

    return count - 1, max_distance