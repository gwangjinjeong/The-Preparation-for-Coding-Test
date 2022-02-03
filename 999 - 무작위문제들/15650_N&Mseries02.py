from sys import stdin
from itertools import combinations as comb

n, m = list(map(int, stdin.readline().split()))
data = [i for i in range(1,n+1)]
result = list(comb(data, m))  # 모든 순열 일렬로 나열
[print(' '.join(list(map(str, i)))) for i in result]