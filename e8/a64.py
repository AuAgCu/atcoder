N, M = map(int, input().split())

graph = {}
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    graph.setdefault(a, [])
    graph[a].append((b, c))
    
    graph.setdefault(b, [])
    graph[b].append((a, c))

import heapq, sys

heap = []
heapq.heapify(heap)
visit = [False] * N
distances = [sys.maxsize] * N
heapq.heappush(heap, (0, 0))

while heap:
    distance, node = heapq.heappop(heap)
    if visit[node]:
        continue

    visit[node] = True
    distances[node] = distance
    for v in graph.get(node, []):
        v_node, v_distance = v

        if not visit[v_node]:
            heapq.heappush(heap, (distance + v_distance, v_node))


for i in range(N):
    if visit[i]:
        print(distances[i])
    else:
        print(-1)