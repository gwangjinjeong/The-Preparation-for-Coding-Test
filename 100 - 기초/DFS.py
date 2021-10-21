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