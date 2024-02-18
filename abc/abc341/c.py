H, W, N = map(int, input().split())

T = input()
s = []
for i in range(H):
  s.append(input())

dic = {
  "L": ( 0, -1),
  "R": ( 0,  1),
  "U": (-1,  0),
  "D": ( 1,  0)
}

ans = 0
for i in range(1, H - 1):
  for j in range(1, W - 1):
  
    nx, ny = i, j
    
    if s[i][j] == '#':
      continue

    exist = True
    for v in T:
      x, y = dic[v]
      nx += x
      ny += y

      if s[nx][ny] == '#':
        exist = False
        break

    if exist:
      ans += 1

print(ans)

