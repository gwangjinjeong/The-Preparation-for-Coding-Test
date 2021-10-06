import sys
from collections import Counter
# 카운터로 다 넣어놓고 dict 쓴다음 둘의 짝 맞으면 통과로 하자 되는거 아님?
# => 아니다. 올바른 괄호형성이 안되기 때문.
# input = sys.stdin.readline

# n = int(input())
# 즉 아래와 같은 방식으로 풀면 안된다.
# for i in range(n):
#     s = list(input())
#     c = Counter(s)
#     if c['('] == c[')']:
#         print('YES')
#     else:
#         print('NO')

# 다시 풀자
# 이것도 안되네 다시 풀자
# input = sys.stdin.readline

# n = int(input())
# for i in range(n):
#     s = list(input())
#     chk = 0
#     for i in s:
#         if i == '(':
#             chk += 1
#         else:
#             chk -=1
#         if chk <0:
#             print('NO')
#     if chk != 0:
#         print('NO')
#     else:
#         print('YES')
# input = sys.stdin.readline

# (가 나오면 )가 나올때까지 찾음
# ) 발견시 (와 )를 해당 인덱스 제거
# 자기 인덱스 이후에 없으면 NO
# (가 없어도 NO
def chk_vps(s):
    if len(s) == 0:
        return 'YES'
    elif s[0] == '(' and ')' in s:
        s.remove('(')
        s.remove(s[s.index(')')])
        return chk_vps(s)
    else:
        return 'NO' 

n = int(input())
for i in range(n):
    s = list(input())
    ns = chk_vps(s)
    print(ns)