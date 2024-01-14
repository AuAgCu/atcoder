n = int(input())

arr = []
arr.append('L')
arr.extend(['o'] * n)
arr.append('ng')

print(''.join(arr))