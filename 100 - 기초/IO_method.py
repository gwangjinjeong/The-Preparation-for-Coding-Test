# 입력

## 데이터 갯수 입력
n = int(input())
print(n)
## 각 데이터 공백으로 구분하여 입력
data = list(map(int, input().split()))
print(data)
## 공백을 기준으로 구분하여 적은 수 입력
n, m, k = map(int, input().split())
print(n,m,k)

## if sys 라이브러리가 허용된다면.
import sys
data = sys.stdin.readline().rstrip()
print(data)

## 응용
data = list(map(int, sys.stdin.readline().rstrip().split()))
print(data)
