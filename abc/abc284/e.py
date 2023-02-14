import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
used = [False for _ in range(N+1)]


def path(dic, current):
    count = 1
    used[current] = True
    for next in dic.get(current, []):
        if used[next]:
            continue

        count += path(dic, next)
        if count >= 10 ** 6:
            print(10 ** 6)
            exit(0)

    used[current] = False

    return count

dic = {}
for i in range(M):
    v, w = map(int, input().split())
    dic.setdefault(w, [])
    dic.setdefault(v, [])
    dic[w].append(v)
    dic[v].append(w)

ans = path(dic, 1)
print(min(10 ** 6, ans))