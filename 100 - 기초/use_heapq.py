import heapq
# 최단 경로 알고리즘 
# 우선순위 큐
# 를 구현하는데 주로 사용하는 라이브러리
# 시간복잡도 O(NlogN)

def heapsort(dataset):
    h = []
    result = []
    for value in dataset:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def maxheapsort(dataset):
    h = []
    result = []
    for value in dataset:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

hs = heapsort([1,3,5,7,9,2,4,6,8,0])
mhs = maxheapsort([1,3,5,7,9,2,4,6,8,0])

print(list(hs))
print(list(mhs))



