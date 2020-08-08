import sys

n = int(input())
a = list(map(int, input().split()))

array = [0 for i in range((10 ** 6)+1)]
for v in a:
  array[v] += 1
  
for i in range(1, len(array)):
  if array[i] == 0:
    continue
    
  for j in range(i*2, len(array), i):
    array[j] = 0
    
count = 0
for v in array:
  if v == 1:
    count += 1
    
print(count)