N, K = map(int, input().split())
c = list(map(int, input().split()))

dic = {}
for i in range(K):
    dic.setdefault(c[i], 0)
    dic[c[i]] += 1

kind = len(dic.keys())
for i in range(K, N):
    dic.setdefault(c[i], 0)
    dic[c[i]] += 1

    delete_index = i - K
    dic[c[delete_index]] -= 1
    if dic[c[delete_index]] == 0:
        dic.pop(c[delete_index])
    
    kind = max(kind, len(dic.keys()))

print(kind)

# TODO: これ問題出す