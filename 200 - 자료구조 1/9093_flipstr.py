import sys

input = sys.stdin.readline 
n = input()
for i in range(int(n)): # n번 반복
    result = []
    s = input().split() # 공백 단위로 split
    for ii in s:        # 하나씩 뽑아서 처리
        result.append(ii[::-1])
    print(' '.join(result))