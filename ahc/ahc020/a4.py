import math

# a2からの変更点
# 辺の橋となっている辺以外をOffにする


def isConnecting(graph, must_points, exclude_points, exclude_edges):
    if len(must_points) == 0:
        return True

    start = must_points[0]
    stack = [start]

    visited = [False for _ in range(len(graph) + 1)]
    while len(stack):
        now = stack.pop()
        visited[now] = True

        for next, _, _ in graph[now]:
            if visited[next] or next in exclude_points or (now, next) in exclude_edges or (next, now) in exclude_edges:
                continue

            stack.append(next)

    for i in range(1, len(visited)):
        if i in must_points and not visited[i]:
            return False

    return True


N, M, K = map(int, input().split())

x, y = [], []
for i in range(N):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

graph = {}
for i in range(M):
    tu, tv, tw = map(int, input().split())
    graph.setdefault(tu, []).append((tv, tw, i))
    graph.setdefault(tv, []).append((tu, tw, i))

a, b = [], []
for i in range(K):
    ta, tb = map(int, input().split())
    a.append(ta)
    b.append(tb)

# 一旦全てONにする
c = [1 for _ in range(M)]
p = [0 for _ in range(N)]
d = {}
for i in range(K):
    near_dis = 5001
    near = -1

    contained = False
    for j in range(N):
        x1, y1 = x[j], y[j]
        x2, y2 = a[i], b[i]
        dis = math.ceil(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
        if dis < p[j]:
            contained = True
            break
        if dis < near_dis:
            near_dis = dis
            near = j

    if contained:
        continue

    p[near] = max(p[near], near_dis)

not_on = []
on = []
for i in range(N):
    if i != 0 and p[i] == 0:
        cost = 0
        for _, c_t, _ in graph[i + 1]:
            cost += c_t

        not_on.append((cost, i + 1))
    else:
        on.append(i + 1)

not_on.sort(reverse=True)
exclude_points = []
for _, point in not_on:
    exclude_points.append(point)
    if isConnecting(graph, on, exclude_points, []):
        for _, _, i in graph[point]:
            c[i] = 0
    else:
        exclude_points.pop()

used_edges = []
for i in on:
    for j, c_t, k in graph[i]:
        if c[k] != 0:
            used_edges.append((c_t, i, j))

used_edges.sort(reverse=True)

exclude_edges = []
for _, i, j in used_edges:
    exclude_edges.append((i, j))
    if isConnecting(graph, on, exclude_points, exclude_edges):
        for index, _, k in graph[i]:
            if index == j:
                c[k] = 0
    else:
        exclude_edges.pop()


p_str = ' '.join(map(str, p))
b_str = ' '.join(map(str, c))

print(p_str)
print(b_str)
