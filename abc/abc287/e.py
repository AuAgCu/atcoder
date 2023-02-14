N = int(input())
arr = []
for i in range(N):
    s = input()
    arr.append(s)

scoreDic = {}
sortedArr = sorted(arr)
for i in range(N):
    s = sortedArr
    score = 0
    if i != 0:
        tmpScore = 0
        for j in range(min(len(s[i-1]), len(s[i]))):
            if s[i-1][j] != s[i][j]:
                break

            tmpScore += 1
        
        score = tmpScore
            

    if i != len(arr) - 1:
        tmpScore = 0
        for j in range(min(len(s[i]), len(s[i+1]))):
            if s[i][j] != s[i+1][j]:
                break
                
            tmpScore += 1

        score = max(tmpScore, score)

    scoreDic[s[i]] = score

for v in arr:
    print(scoreDic[v])