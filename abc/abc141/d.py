import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(len(a)):
    a[i] *= -1

heapq.heapify(a)

for i in range(m):
    tmp = heapq.heappop(a)
    heapq.heappush(a, tmp/2)

ans = -1 * sum(map(int, a))

print(ans)