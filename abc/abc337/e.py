import math

# def ap(arr):
#   for v in arr:
#     print('debug: ', v)

N = int(input())

m = math.ceil(math.log2(N))
print(m)

arr = []
for i in range(N):
  tmp = bin(i)[2:].zfill(m)
  arr.append(tmp)

hitos = []
for i in range(m):
  hito = []
  for j in range(N):
    if arr[j][i] == '1':
      hito.append(str(j + 1))

  hitos.append(hito)


for hito in hitos:
  print(len(hito), ' '.join(hito))

s = input()

# ap(hitos)
bits = []
for i in range(len(s)):

  if s[i] == '1':
    bit = 0
    for j in range(len(hitos[i])):
      bit += 2 ** (int(hitos[i][j]) - 1)

  else:
    bit = 2 ** N - 1
    for j in range(len(hitos[i])):
      bit -= 2 ** (int(hitos[i][j]) - 1)

  bits.append(bit)

ans = bits[0]
for i in range(1, len(bits)):
  ans = ans & bits[i]

print(math.ceil(math.log2(ans)) + 1)