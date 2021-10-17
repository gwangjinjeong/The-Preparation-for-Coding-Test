# 초콜릿 정사각형 N개 2제곱형태
# K개를 먹어야 안졸음
# K개로 쪼갬
# 2개를 8번쪼갯다고? -> 6개 먹을껀데 친구  8 2 => 8+4 = 12개 즉, 상근이가 6개 선영이가 나머지 6개 먹는것.
#x + x/2^y = N*2
import sys
import math
N = sys.stdin.readline() # 6
n = math.log2(int(N)) # 2.5
cnt = 1
if int(n) == n:
    n = int(n)
    cnt = 0
else:
    n = int(n) + 1
    for i in reversed(range(n)):
        if int(N) == 0:
            break
        elif int(N) < pow(2, i):
            cnt += 1
        elif int(N) > pow(2, i): # 6-4(8/2) = 2
            N = int(N) - pow(2, i) # 6 - 4 = 2
            cnt += 1
        else:
            break

print(pow(2, int(n)), cnt)