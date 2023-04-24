N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 料理1つに対して(おいしさ、嫌いか)のタプルの配列を作成する。
tuples = []
for i, oisisa in enumerate(a):
    if i + 1 in b:
        tuples.append((oisisa, True))
    else:
        tuples.append((oisisa, False))

# タプルをソートすると,1個目の要素（今回でいうとおいしさ）でソートされるのでそれを利用する。
# おいしさの降順でソート（おいしさが高いものを先頭に持ってくる）
tuples.sort(reverse=True)

max_oisisa = tuples[0][0]
for tuple in tuples:
    oisisa, kirai = tuple
    if oisisa != max_oisisa:
        break

    # 嫌いなものだった場合、Yesを出して終了。
    if kirai:
        print("Yes")
        exit(0)

print("No")
