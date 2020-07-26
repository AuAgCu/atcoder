a,b,c = map(int,input().split())
k = int(input())

count = 0
while b <= a:
  b *= 2
  count += 1
  
while c <= b:
  c *= 2
  count += 1
  
print('Yes' if k>=count else 'No')
