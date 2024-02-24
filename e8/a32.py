N, A, B = map(int, input().split())

array = [None] * (N + 1)

for i in range(N + 1):
  index_a = i - A
  index_b = i - B

  ## flag= True で勝ち
  a_flag = (i - A) >= 0 and array[i - A]
  b_flag = (i - B) >= 0 and array[i - B]

  array[i] = not (a_flag or b_flag)

print('First' if not array[-1] else 'Second')

# print(array)