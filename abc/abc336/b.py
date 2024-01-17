count = 0
n = int(input())

while n % 2 == 0:
  count += 1
  n //= 2

print(count)