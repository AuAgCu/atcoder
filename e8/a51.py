Q = int(input())

stack = []
for _ in range(Q):
  q = input().split()
  if q[0] == '1':
    stack.append(q[1])
  elif q[0] == '2':
    print(stack[-1])
  else:
    stack.pop()
