N = int(input())

last = (0, 0, 0)

success = True
for i in range(N):
  t2, x2, y2 = map(int, input().split())
  t1, x1, y1 = last
  
  dt = t2 - t1
  distance = abs(x2 - x1) + abs(y2 - y1)
  
  last = t2, x2, y2

  #  最短距離で行っても時間が足りないか、到着した後の時間が奇数だとうまく足踏みできない
  if dt < distance or (dt - distance) % 2 != 0:
    success = False
    break
    
print('Yes' if success else 'No')
  