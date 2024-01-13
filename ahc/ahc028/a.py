import sys
import time
import copy



debug = False
def p(*arr):
  if debug:
    print(*arr)

def ans_print(saiteki):
  p(saiteki)
  for v in saiteki:
    print(v[1], v[2])

def point(s, dic):
  px, py = S1, S2

  max_cost = sys.maxsize
  saiteki = []
  while True:
    end = time.time()
    diff = end - start
    
    if diff > 1.95:
      # ここに出力する処理を書く
      ans_print(saiteki)
      sys.exit(0)

    sum_cost = 0
    pr = []
    for c in s:
      cost = sys.maxsize
      for v in dic[c]:
        x, y = v
        t_cost = abs(px - x) + abs(py - y) + 1

        if cost > t_cost:
          cost = t_cost
          tx, ty = x, y
        
      sum_cost += cost
      pr.append((sum_cost, tx, ty))
      px, py = tx, ty

    if sum_cost < max_cost:
      saiteki = pr
      p(saiteki)
      max_cost = sum_cost
      
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
        p(s1, s2, words[j])
        mc = max(mc, len(s1))
        head = False
        break

    if max_cover < mc:
      max_cover = mc
      selected = j
      is_head = head

  p(max_cover, words[selected], s[:5], s[-5:], i, selected, is_head)
  words[i], words[selected] = words[selected], words[i]
  if is_covered:
    pass
  elif is_head:
    s = words[i][:word_l - max_cover] + s
  else:
    s += words[i][max_cover:]
      
p(s)
p(len(s))
point(s, dic)