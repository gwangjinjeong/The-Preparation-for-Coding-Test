# 입력은 간선들의 수를 받아서 처리해야한다.
# 그렇다면 인접행렬보다 인접리스트로 만들어서 처리한는것이 편하지 않을까?
# 그니까 아이디어가 인접 행렬을 만들어서 처리하겠다?
# 정점의 갯수가 많으면 불리할거같다.
# 하지만 정점의 갯수가 1000개 이하이기 때문에 인접행렬로 진행하자.
from collections import deque

# def dfs(SN, queue, visited):  # Start node, Queue, 방문한노드인지 체크
#     if visited[SN]:
#         return 0
#     else:
#         visited[SN] = True
#         print(SN, end=' ')
#         for vv in queue:
#             nodes = []
#             for v in queue:
#                 if v[0] == SN:
#                     nodes.append(v)
#             queue.remove(min(nodes))
#             dfs(min(nodes)[1], queue, visited)
#     return 0

def dfs(sn, am, v):  # Start node, Queue, 방문한노드인지 체크
    if v[sn]:
        return 0
    else:
        v[sn] = True
        print(sn, end=' ')
        for i in range(1, len(am)):
            if not v[i] and am[sn][i]: # 방문안했고, 해당행렬에 1이 있으면 재귀
                dfs(i, am, v)
    return 0

def bfs(sn, am, v):
    queue = deque([sn])
    v[sn] = 0
    while(queue):
        h = queue.popleft() # queue[0]
        print(h, end=' ')
        # queue.remove(h)
        for i in range(1, len(am)):
            if v[i] and am[h][i] == 1:
                queue.append(i)
                v[i] = 0

v, e, sv = list(map(int, input().split()))
am = [[0]*(v+1) for _ in range(v+1)]
visited = [False] * (v + 1)
for _ in range(e):  # 양방향처리
    x, y = list(map(int, input().split()))
    am[y][x] = am[x][y] = 1
dfs(sv, am, visited)
print()
bfs(sv, am, visited)