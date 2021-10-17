# S -> T
# 문자열 뒤 A
# 문자열 뒤집고 뒤 B
# 만들수 있으면 1 없으면 0
# TC: B / ABBA => BA => ABB => ABBA ====> 1
# TC: B / BBA => BB => BBA
# TC: B / ABBB => BB => BBA => ABBB
# TC: AB ABB => 0

# import sys
# def cal_play(S,T):
#     if S == T:
#         return 1
#     elif (len(S) > len(T)):
#         return 0
#     else:
#         a = cal_play(S+'A',T)
#         b = cal_play(S[::-1]+'B',T)
#         return a+b
#
# S = sys.stdin.readline().rstrip()
# T = sys.stdin.readline().rstrip()
#
# print(cal_play(S,T))

## ---- 시간초과
import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

while(True):
    if len(S) == len(T):
        a = 1 if S == T  else 0
        print(a)
        break
    else:
        if T[-1] == 'A':
            T = T[:-1]
            continue
        else:
            T = T[:-1][::-1]
            continue
