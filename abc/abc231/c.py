import bisect

N, Q = map(int, input().split())
height_arr = list(map(int, input().split()))

height_arr.sort()
# 計算量はN log N になるので、十分間に合う
for _ in range(Q):
    x = int(input())
    # 今回一番大事な部分、2分探索をすることで計算量をN → log N にする
    # height_arr=[2, 4, 6, 8, 10], x=5の時はindex=2となる
    index = bisect.bisect_left(height_arr, x)

    print(N - index)
