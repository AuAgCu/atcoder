N, M = map(int, input().split())

dic = {}

for i in range(M):
    a, b = map(int, input().split())
    dic.setdefault(a, [])
    dic.setdefault(b, [])

    dic[a].append(b)
    dic[b].append(a)

for i in range(1, N + 1):
    array = dic.get(i, [])

    ans = [len(array)]
    ans.extend(sorted(array))
    print(' '.join(map(str, ans)))