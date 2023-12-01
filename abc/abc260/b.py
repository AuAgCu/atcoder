N, X, Y, Z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tupples = []
for i in range(N):
    # (受験番号、数学の点数、英語の点数)のtuppleを作成
    tupple = (i + 1, a[i], b[i])
    tupples.append(tupple)

goukaku = []

# 数学の昇順、受験番号の降順でソート
tupples.sort(key=lambda x: (x[1], -x[0]))
# 後ろの人が先に受かるので、後ろからX人取り出す
for _ in range(X):
    number, _, _ = tupples.pop()
    goukaku.append(number)

# 英語の昇順、受験番号の降順でソート
tupples.sort(key=lambda x: (x[2], -x[0]))
for _ in range(Y):
    goukaku.append(tupples.pop()[0])

# 数学と英語の合計の昇順、受験番号の降順でソート
tupples.sort(key=lambda x: (x[1] + x[2], -x[0]))
for _ in range(Z):
    goukaku.append(tupples.pop()[0])

goukaku.sort()

print('\n'.join(map(str, goukaku)))





