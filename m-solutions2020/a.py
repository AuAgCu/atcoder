x = int(input()) - 400

count = 8

while True:
  
  if x < 200 or count == 1:
    break
    
  count -= 1
  x -= 200
  
print(count)

