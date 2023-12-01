from collections import deque

R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

sx -= 1
sy -= 1
gx -= 1
gy -= 1

m = []
for i in range(R):
    m.append(input())

dist = [[-1 for i in range(R)] for i in range(C)]

moves = [
    (0, 1), 
    (0, -1), 
    (1, 0), 
    (-1, 0)
]

q = deque()
q.append((sx, sy, 0))
while q:
    x, y, d = q.popleft()

    if dist[y][x] != -1:
        continue

    dist[y][x] = d

    if y == gy and x == gx:
        print(d)
        exit(0)

    for v in moves:
        dx, dy = v

        if m[x+dx][y+dy] == '#':
            continue

        q.append((x + dx, y + dy, d + 1))
