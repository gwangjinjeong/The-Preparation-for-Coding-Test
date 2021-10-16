import sys
# N개 라면 공장중 i번째에서 Ai개를 구매
# 1. i번째 1구매 => cost = 3
# 2. i, i+1 1구매 => cost = 5
# 3. i, i+1, i+2 구매 => cost = 7
# 최소 비용 구매, output = 필요금액
# 파이썬 1초당 2000만 즉, 1000만 까지 연산 가능


#### 틀린이유: 숫자가 1만 나오는게 아닌데 1로만 생각해버렸다.
# N = sys.stdin.readline()
# com = list(map(str, input().split()))
# s = ''.join(com)
# cost = 0
# while(True):
#     if '111' in s:
#         cost += 7
#         idx = s.index('111')
#         if len(s) - idx == 3:
#             s = s[0:idx]
#         elif idx == 0:
#             s = s[idx+3:]
#         else:
#             s = s[:idx] + s[idx+2:len(s)]
#     elif '11' in s:
#         cost += 5
#         idx = s.index('11')
#         if len(s) - idx == 2:
#             s = s[0:idx]
#         elif idx == 0:
#             s = s[idx+2:]
#         else:
#             s = s[:idx] + s[idx + 1:len(s)]
#     else:
#         cost += sum(list(map(int, s)))*3
#         break
#
# print(cost)

#### 재시도 틀림, 반례 2 3 2 1 https://blog.koderpark.dev/30
# 테스트 케이스 1 1 2 1 (0) => 0 0 1 1 (7) => 0 0 0 0 (12)
# 0 단위로 split해서 만약 없다면? 맨 앞 index부터 3개 숫자 찾아가자.
#
import sys
def calcul(com, cost):
    s = ''.join(com) # 1. 리스트로 받은걸 0으로 나눠 ex) ['3','1','0','3'](com) -> 3103
    ss = s.split('0')
    len_list = [len(i) for i in ss] # 각 나눈것들의 len 구함 ex) ['31','3'] => [2,1]
    for k, i in enumerate(len_list):
        if i == 0:
            continue
        elif i == 1:
            cost += int(ss[k]) * 3
            ss[k] = '0'
        elif i == 2:
            l2 = list(map(int,list(ss[k])))
            m2 = min(l2)
            cost += int(m2) * 5
            new_l2 = [ii - m2 for ii in l2]
            com, cost = calcul(list(map(str, new_l2)), cost)
        elif i >= 3:
            l3 = list(map(int, list(ss[k])))
            m3 = min(l3[:3])
            cost += int(m3) * 7
            l3[:3] = [ii - m3 for ii in l3[:3]]
            com, cost = calcul(list(map(str, l3)), cost)
    return com, cost

N = sys.stdin.readline()
com = list(map(str, input().split()))
cost = 0
result_cost = calcul(com, cost)
print(result_cost[1])


