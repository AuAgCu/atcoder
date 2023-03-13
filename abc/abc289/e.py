from collections import deque

def resolve():
    N, M = map(int, input().split())
    used = [[False for _ in range(N+1)] for _ in range(N+1)]

    c = [-1] + list(map(int, input().split()))
    dic = {}
    for _ in range(M):
        v, w = map(int, input().split())
        dic.setdefault(v, [])
        dic.setdefault(w, [])

        dic[v].append(w)
        dic[w].append(v)

    d = deque([(1, N, 0)])
    ans = -1
    while len(d):
        takahashi, aoki, count = d.popleft()
        if takahashi == N and aoki == 1:
            ans = count
            break

        if used[takahashi][aoki]:
            continue

        used[takahashi][aoki] = True
        for v in dic.get(takahashi, []):
            for w in dic.get(aoki, []):
                if c[v] != c[w]:
                    d.append((v, w, count + 1))

        
    print(ans)

T = int(input())
for _ in range(T):
    resolve()