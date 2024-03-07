N, K = map(int, input().split())
KI = 100

dic_a = {}
dic_b = {}
for i in range(N):
    a, b = map(int, input().split())
               
    dic_a.setdefault(a, [])
    dic_a[a].append(i)

    dic_b.setdefault(b, [])
    dic_b[b].append(i)

a_set = set()
for i in range(1, K + 2):
    a_set |= set(dic_a.get(i, []))

ans = 0
for i in range(1, KI - K + 2):
    b_set = set()
    for j in range(1, K + 2):
        b_set |= set(dic_b.get(j, []))

    for j in range(1, KI - K + 2):
        count = len(a_set & b_set)

        if count > ans:
            # print(i, j)
            # print(a_set)
            # print(b_set)
            # print(a_set & b_set)
            ans = count

        # print(i, i + K, j, j + K, a_set, b_set)
        b_set -= set(dic_b.get(j, []))
        b_set |= set(dic_b.get(j + K + 1, []))

    a_set -= set(dic_a.get(i, []))
    a_set |= set(dic_a.get(i + K + 1, []))

print(ans)