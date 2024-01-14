N = int(input())
A = list(map(int, input().split()))
arr = [A[0]]
r_arr = [A[-1]]

for v in A[1:]:
  arr.append(max(v, arr[-1]))

for v in reversed(A[:-1]):
  r_arr.append(max(v, r_arr[-1]))

r_arr.reverse()

D = int(input())
for _ in range(D):
  l, r = map(int, input().split())
  l -= 2
  print(max(arr[l], r_arr[r]))