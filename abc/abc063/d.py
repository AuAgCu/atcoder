import math

def func(h, a, b, count):
  ans = 0
  for v in h:
    if v > b * count:
      ans += math.ceil((v-b*count) / (a-b))
      
  return ans <= count

n,a,b = map(int, input().split())
h = []

for i in range(n):
  # heapqを最大値を取り出すように使いたいのでマイナスにする
  h.append(int(input()))

start = 1
end = math.ceil(max(h) / b)
middle = (end + start) // 2

# 二分探索する、終了条件はぶっちゃけわからん
while True:
  if(func(h,a,b,middle)):
    end = middle
  else:
    start = middle
    
  middle = (end + start) // 2
  if (end - start) <= 1:
    break
    
print(end)