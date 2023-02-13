n = int(input())
a = list(map(int, input().split()))

# 初期化
last = 0
cuts = [0]
for v in a:
    # 最初の位置を0として、切り込みを入れる位置を記録する。
    # 360で割った余りを入れると1周しても切り込みの位置が記録できる
    # 例: 375度→15度
    cut = (last + v) % 360
    cuts.append(cut)

    last = cut

print(cuts)
# ここで360度を入れておくと後々楽
cuts.append(360)
cuts.sort()

print(cuts)

ans = 0
for i in range(1, len(cuts)):
   ans = max(ans, cuts[i] - cuts[i-1])

print(ans)