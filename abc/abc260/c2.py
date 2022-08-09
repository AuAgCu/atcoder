N, X, Y = map(int, input().split())

red, blue = 1, 0

for i in range(N-1):
    # まず赤ジェムを変換
    blue += red * X # blueは赤ジェム * Xだけ増える(ここに入る数はまだ赤ジェムと同レベル)
    next_red = red # 赤ジェムは同個数になる

    # 青ジェムを変換
    next_red += blue # 赤ジェムは青ジェムの数だけ増える
    next_blue = blue * Y

    blue = next_blue
    red = next_red

print(blue)
