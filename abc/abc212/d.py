import heapq

heap = []
count = 0

Q = int(input())

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heapq.heappush(heap, q[1] - count)
    elif q[0] == 2:
        count += q[1]
    else:
        print(heapq.heappop(heap) + count)
