a, b, c, d, e, f, x = map(int, input().split())

# 走る→休憩のループを行う回数
count_takahashi = x // (a + c)
count_aoki = x // (d + f)

# 余った秒数
diff_takahashi = x -  count_takahashi * (a + c)
diff_oki = x -  count_aoki * (d + f)

# a * bが一回のループで走る距離なので、それにcountをかける.それプラス余った時間で走った距離を足せば良い
distance_takahashi = a * b * count_takahashi + min(diff_takahashi, a) * b
distance_aoki = d * e * count_aoki + min(diff_oki, d) * e

if distance_takahashi == distance_aoki:
    result = 'Draw'
elif distance_takahashi > distance_aoki:
    result = 'Takahashi'
else:
    result = 'Aoki'

print(result)