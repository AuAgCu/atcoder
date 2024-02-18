
# LとRの間のみ、1、それ以外は0のbitを生成する。
def huga(L, R):
  return 2 ** (L + 1) - 1 - (2 ** R - 1)

N, Q = map(int, input().split())
ss = input()

s = int(ss, 2)
for i in range(Q):
  n, L, R = map(int, input().split())
  L = N - L 
  R = N - R

  if n == 1:
    hoge = huga(L, R)
    s = s ^ hoge

    # print('after: ', bin(s))


  if n == 2:
    if L == R:
      print('Yes')
      continue
    
    hoge = huga(L, R)
    tmp = s & hoge
    tmp //= 2 ** R
    tmp2 = tmp * 2

    tmp3 = tmp2 ^ tmp
    tmp3 //= 2
    # tmp3 += 1
    # print(bin(tmp))
    # print(bin(tmp2))
    # print(bin(tmp3))

    # print("冪乗数調査", tmp3, beki2(tmp3))
    tmp4 = 2 ** (len(bin(tmp3)) - 2) - 1

    # print(tmp3, tmp4)
    # print(tmp3, tmp4)
    print('Yes' if tmp3 ^ tmp4 == 0 else 'No')
