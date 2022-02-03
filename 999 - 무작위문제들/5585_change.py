# 돈(1 이상 1000미만의 정수) 1개
# 카운터에서 1000엔 지폐를 한장 냈을 때
# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
# TC: 380 => 620 == 500x1 100x1 0x2 => 4
# TC: 1 => 999 == 500x1 100x4 50x1 10x4 5x1 1x4 = 15
import sys

N = sys.stdin.readline()
pay = 1000 - int(N)
changes = 0
if pay >= 500:
    changes = changes + pay // 500
    pay = pay % 500
if pay >= 100:
    changes = changes + pay // 100
    pay = pay % 100
if pay >= 50:
    changes = changes + pay // 50
    pay = pay % 50
if pay >= 10:
    changes = changes + pay // 10
    pay = pay % 10
if pay >= 5:
    changes = changes + pay // 5
    pay = pay % 5
if pay >= 1:
    changes = changes + pay // 1
    pay = pay % 1

print(changes)


