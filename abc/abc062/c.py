import sys

def func(h, w):
  ans = sys.maxsize
  h3 = h // 3
  fragments = []
  fragments.append(h3*w)

  if w % 2 == 0:
    fragments.append((h-h3) * w//2)
  else:
    fragments.append((h-h3) * w//2)
    fragments.append((h-h3) * (w//2 + 1))
    
  ans = min(ans, max(fragments) - min(fragments)) 
  
  h3 += 1
  fragments = []
  fragments.append(h3*w)
  if w % 2 == 0:
    fragments.append((h-h3) * w//2)
  else:
    fragments.append((h-h3) * (w//2))
    fragments.append((h-h3) * (w//2 + 1))
    
  ans = min(ans, max(fragments) - min(fragments))
  
  return ans
  

h,w = map(int, input().split())

# hかwが3で割り切れる場合は0
if h % 3 == 0 or w % 3 == 0:
  print(0)
  sys.exit()

# 縦に2回割る場合はhが差分、横に2回割る場合はwが差分となるので小さい方が正解候補
ans = min(w, h)

# 横1回,縦1回で割る場合
ans = min(func(h,w), func(w,h), ans)

print(ans)