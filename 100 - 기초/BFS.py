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