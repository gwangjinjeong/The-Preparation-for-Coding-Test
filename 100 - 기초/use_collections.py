from collections import deque,Counter
# deque을 이용해서 큐를 구현해야한다. 시간복잡도가 O(1) 이기 떄문에 
# 특징: 인덱싱, 슬라이싱 기능은 사용 X
# 첫 번째 원소 제거 : popleft()
# 마지막 원소 제거 : pop()
# 첫 번째 원소 삽입 : appendleft()
# 마지막 원소 삽입 : append(x)

## 1. deque
data = deque([2,3,4])
print(data)
data.appendleft(1)
print(data)
data.append(5)

print(data)
print(list(data))

## 2.Counter
counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(counter['red'])
print(dict(counter))
print(list(counter.values()))