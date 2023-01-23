# TLEする実装、O(N*Q)なのでだめ
N, Q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(Q):
    x = int(input())
    
    count = 0
    for height in a:
        if height >= x:
            count += 1

    print(count)