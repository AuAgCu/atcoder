n, k = map(int, input().split())
s = []
for i in range(n):
  s.append(int(input()))
  
seki = s[0]
head = 0
tail = 0

ans = 0
while head <= n - 1:
  print(head, tail, seki)
  if s[head] > k:
    head += 1
    tail = head
    seki = s[head]
    continue
    
  if seki <= k:
    if head - tail + 1 > ans:
      print("update:", head, tail)
    
    ans = max(head - tail + 1, ans)
    head += 1

    if head == n:
      break

    seki *= s[head]
  else:
    seki //= s[tail]
    tail += 1
    
print(ans)
