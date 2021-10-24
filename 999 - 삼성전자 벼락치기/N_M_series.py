import sys
# 31
# 1 \ 2 \ 3
# 3 2
# 1 2 \ 1 3 \ 2 1 \ 2 2 \ 2 3

N, M = map(int, input().split())

visit = [False] * (N+1)

result = []

def nm1(cur,N,M):
    if cur == M:
        print(' '.join(result))
        return 0
    for i in range(1, N+1):
        if not visit[i]:
            visit[i] = True
            result.append(str(i))
            nm1(cur+1,N,M)
            visit[i] = False
            result.pop()
nm1(0,N,M)