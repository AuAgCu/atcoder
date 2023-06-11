import math

N, M, K = map(int, input().split())

x, y = [], []
for i in range(N):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

u, v, w = [], [], []
for i in range(M):
    tu, tv, tw = map(int, input().split())
    u.append(tu)
    v.append(tv)
    w.append(tw)

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

p_str = ' '.join(map(str, p))
b_str = ' '.join(map(str, c))

print(p_str)
print(b_str)
