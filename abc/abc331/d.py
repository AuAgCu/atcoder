import math

debug = True

def p(*arr):
    if not debug:
        return
    
    print(arr)

def array_print(arr):
    for v in arr:
        p(v)

N, Q = map(int, input().split())

bw_arr = []
for i in range(N):
    bw_arr.append(input())

# 初期値
imosu = [[0] * (N + 1)]
for i in range(N):
    arr = [0]
    for j in range(N):
        ue = imosu[i][j + 1] - imosu[i][j]
        if bw_arr[i][j] == 'B':
            arr.append(ue + arr[-1] + 1)
        else:
            arr.append(ue + arr[-1])

    imosu.append(arr)

imosu = imosu[1:]
for i in range(len(imosu)):
    imosu[i] = imosu[i][1:]

array_print(imosu)

for i in range(1):
    a, b, c, d = map(int, input().split())

    ta = math.ceil(a / N) * N
    tb = math.ceil(b / N) * N
    tc = (c + 1) // N * N
    td = (d + 1) // N * N

    # 四角形をまず計算
    square = ((tc - ta) // N) * ((td - tb) // N) * imosu[-1][-1]
    p('四角', square)

    # 余った左を計算
    left = ((imosu[-1][-1] - imosu[-1][(b - 1) % N])) * (tc - ta) // N
    p('左', left)

    # 余った右を計算
    right = (imosu[-1][(d + 1) % N] - imosu[-1][td % N]) * (tc - ta) // N
    p('右', right,(imosu[-1][(d + 1) % N]), imosu[-1][td % N])

    # 余った上を計算
    up = ((imosu[-1][-1]) - (imosu[(a - 1) % N][-1])) * (td - tb) // N
    p('上', up)

    # 余った下を計算
    down = (imosu[c % N][-1])* (td - tb) // N
    p('下', down)

    # 左上
    left_up = (imosu[-1][-1]) - (imosu[(a - 1) % N][-1]) - ((imosu[-1][(tb - 1) % N]) - (imosu[(a - 1) % N][b % N]))
    p('左上', left_up, (imosu[-1][-1]) - (imosu[(a - 1) % N][-1]), ((imosu[-1][(tb - 1) % N]) - (imosu[(a - 1) % N][b % N])))

    # 右上
    right_up = (imosu[-1][(d % N)] - imosu[(a - 1) % N][d % N])
    p('右上', right_up, (-1, d % N), ((a - 1) % N, d % N))

    # 左下
    left_down = (imosu[c % N][-1] - imosu[c % N][(b - 1) % N])
    p('左下', left_down, (c % N, -1), (c % N, (b - 1) % N))

    # 右下
    right_down = (imosu[c % N][d % N])
    p('右下', right_down)

    ans = square + left + right + up + down + left_up + right_up + left_down + right_down
    p(ta, tb, tc, td)
    p('ans', ans)

    print(ans)
    