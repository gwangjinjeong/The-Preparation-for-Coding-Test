from  bisect import bisect_left, bisect_right
# bisect_left : 리스트 a에 정렬된 순서를 유지하며 삽입할 x에 대해 적절한 가장 왼쪽 인덱스 찾기
# bisect_right : 리스트 a에 정렬된 순서를 유지하며 삽입할 x에 대해 적절한 가장 오른쪽 인덱스 찾기

# example 1 사용법
a = [1,2,3,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

# example 2 입력된 2개의 숫자 사이 요소 갯수 구하기
def count_element_between_a_and_b(dataset,a,b):
    lft = bisect_left(dataset,a)
    rgt = bisect_right(dataset,b)
    return abs(rgt -lft)

print(count_element_between_a_and_b(a,8,3))