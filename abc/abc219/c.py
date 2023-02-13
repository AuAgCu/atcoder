s = input()

dic = {}
dic_reverse = {}

# 普通のabc順
alphabet = ""
for i in range(97, 123):
    c = chr(i)
    alphabet += c

for i in range(len(s)):
    c = alphabet[i]
    c_r = s[i]
    dic[c_r] = c
    dic_reverse[c] = c_r

names = []
N = int(input())
for _ in range(N):
    name = input()

    coverted_name = ''.join(map(lambda x: dic[x], name))
    names.append(coverted_name)

names = sorted(names)
for name in names:
    reversed_name = ''.join(map(lambda x: dic_reverse[x], name))
    print(reversed_name)
