import sys

N = int(input())

dic = {}
for i in range(N):
  l, r = map(int, input().split())
  dic.setdefault(l, r)
  if dic[l] > r:
    dic[l] = r

count = 0
end = None
for i in range(86400 + 1):
  if end != None and end == i:
    count += 1
    end = None

  next = dic.get(i, sys.maxsize)
  if end == None or next < end:
    end = next
  
print(count)
    