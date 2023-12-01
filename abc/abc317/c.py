import copy

memo = {}
N, M = map(int, input().split())

graph = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c  = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

init_array = [False for _ in range(N)]
stack = [(i, 0, copy.deepcopy(init_array)) for i in range(N)]
max_distance = 0
while stack:
    p, distance, visited = stack.pop()
    visited[p] = True

    k = ','.join(list(map(str, visited))) + str(p)

    max_distance = max(max_distance, distance)
    if k not in memo or memo[k] < distance:
        memo[k] = distance
    else:
        continue
    
    for i in range(N):
        if graph[p][i] == -1 or visited[i]:
            continue
        
        stack.append((i, distance + graph[p][i], copy.deepcopy(visited)))

print(max_distance)
