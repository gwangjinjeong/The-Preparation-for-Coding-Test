# 모험가 길드
# TC
# [2 3 1 2 2] => 2
# [1 1 4 2 2 1] => 3(X), 4(O)
# 가장 작은 값 찾고
import heapq
def heapsort(dataset):
    h = []
    result = []
    for value in dataset:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def explorer(N):
    s_tmp = heapsort(N)
    result = 0
    cur = 0
    while(1):
        cur += s_tmp[cur]
        if cur >= len(s_tmp):
            break
        result += 1
    return result
print(explorer([1,1,4,2,2,1]))


def explorer_dongbinna(N):
    N.sort()
    result = 0
    cnt = 0
    for i in N:
        cnt += 1
        if cnt >= i:
            result += 1
            cnt = 0
    return result
print(explorer_dongbinna([1,1,4,2,2,1]))
