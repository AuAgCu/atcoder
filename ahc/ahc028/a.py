import sys
import time
import copy
import random

debug = False
def p(*arr):
  if debug:
    print(*arr)

def ans_print(saiteki):
  for v in saiteki:
    print(v[1], v[2])

def low_cost(s, arr):
  if len(s) == len(arr) - 1:
    return arr

  sum_cost, px, py = arr[-1]
  c = s[len(arr) - 1]
  cost = sys.maxsize
  for v in dic[c]:
    x, y = v
    t_cost = abs(px - x) + abs(py - y) + 1

    if cost > t_cost:
      cost = t_cost
      tx, ty = x, y

  sum_cost += cost
  arr.append((sum_cost, tx, ty))
  return low_cost(s, arr)

def ans_first(s, dic):
  return low_cost(s, [(0, S1, S2)])

def point(s, dic):
  max_cost = sys.maxsize
  saiteki = ans_first(s, dic)
  while time.time() - start < 1.95:
    sum_cost, _, _ = saiteki[-1]
    
    index = random.randrange(len(s))
    c = s[index]
    for position in dic[c]:
      arr = copy.deepcopy(saiteki[:index])
      cost, x, y = arr[-1]
      nx, ny = position

      n_cost = cost + abs(nx - x) + abs(ny - y) + 1
      arr.append((n_cost, nx, ny))
      tmp = low_cost(s, arr)

      p('newCost:', tmp[-1][0])
      p('nowCost:', sum_cost)
      if tmp[-1][0] < sum_cost:
        saiteki = tmp
        sum_cost = tmp[-1][0]

  ans_print(saiteki)
      
N, M = map(int, input().split())
S1, S2 = map(int, input().split())

arr = []
dic = {chr(i): [] for i in range(ord('A'), ord('Z') + 1)}
for i in range(N):
  v = input()
  for j in range(len(v)):
    dic[v[j]].append((i, j))

  arr.append(v)

words = []
for _ in range(M):
  words.append(input())

start = time.time()
word_l = 5
s = words[0]
for i in range(1, M):
  selected = i
  max_cover = 0
  is_head = True
  is_covered = False
  for j in range(i, M):
    # 文字列が既に存在する場合は選択
    if words[j] in s:
      selected = j
      is_covered = True
      break

    # とりあえず重なりが大きいものを選択していく
    # まず先頭
    mc = 0
    head = True
    for k in range(1, word_l):
      if mc >= word_l - k:
        break

      s1 = words[j][k:]
      s2 = s[:len(s1)]
      if s1 == s2 and mc < len(s1):
        mc = max(mc, len(s1))
        break

    # 後ろから
    for k in range(1, word_l):
      if mc >= word_l - k:
        break

      s1 = words[j][:word_l - k]
      s2 = s[-word_l + k:]

      if s1 == s2 and mc < len(s1):
        mc = max(mc, len(s1))
        head = False
        break

    if max_cover < mc:
      max_cover = mc
      selected = j
      is_head = head

  words[i], words[selected] = words[selected], words[i]
  if is_covered:
    pass
  elif is_head:
    s = words[i][:word_l - max_cover] + s
  else:
    s += words[i][max_cover:]
      
point(s, dic)