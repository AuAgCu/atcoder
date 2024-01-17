N, Q = map(int, input().split())
C = list(map(int, input().split()))

boxes = []
for v in C:
  boxes.append(set([v]))

for _ in range(Q):
  a, b = map(int, input().split())
  a -= 1
  b -= 1

  boxes[b] = boxes[b] | boxes[a]
  boxes[a] = set()

  print(len(boxes[b]))