import heapq, sys

H, W = map(int, input().split())
s = []

s.append('#' * (W+4))
s.append('#' * (W+4))
for _ in range(H):
    s.append('##' + input() + '##')
s.append('#' * (W+4))
s.append('#' * (W+4))

heap = []
#(回数, h, w)のタプル
heapq.heappush(heap, (0, 2, 2)) 

array = [[-1 for _ in range(W+4)] for _ in range(H+4)]
while len(heap):
    c, i, j = heapq.heappop(heap)
    if i <= 1 or j <= 1 or i >= H+3 or j >= W+3:
        continue

    if array[i][j] != -1:
        continue

    array[i][j] = c

    if i == H+1 and j == W+1:
        break

    if s[i][j-1] == '.':
        heapq.heappush(heap, (c, i, j-1))
    else:
        for w in range(1, 3):
            for h in range(i-1, i+2):
                heapq.heappush(heap, (c+1, h, j-w))

    if s[i][j+1] == '.':
        heapq.heappush(heap, (c, i, j+1))
    else:
        for w in range(1, 3):
            for h in range(i-1, i+2):
                heapq.heappush(heap, (c+1, h, j+w))
    
    if s[i-1][j] == '.':
        heapq.heappush(heap, (c, i-1, j))
    else:
        for h in range(1, 3):
            for w in range(j-1, j+2):
                heapq.heappush(heap, (c+1, i-h, w))

    if s[i+1][j] == '.':
        heapq.heappush(heap, (c, i+1, j))
    else:
        for h in range(1, 3):
            for w in range(j-1, j+2):
                heapq.heappush(heap, (c+1, i+h, w))

print(c)