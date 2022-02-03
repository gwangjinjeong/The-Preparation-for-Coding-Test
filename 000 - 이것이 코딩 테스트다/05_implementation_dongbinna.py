# King knight
# TC a1 -> 2
#    c2 -> 6
# 수평 2칸 + 수직 1칸
# 수직 2칸 + 수평 1칸
def kingKnight(S):
    x = ord(S[0]) - 96
    y = int(S[1])
    cnt = 0
    if x - 2 > 0 and y - 1 > 0:
        cnt+=1
    if x - 2 > 0 and y + 1 > 0:
        cnt += 1
    if x + 2 > 0 and y - 1 > 0:
        cnt += 1
    if x + 2 > 0 and y + 1 > 0:
        cnt += 1
    if x - 1 > 0 and y - 2 > 0:
        cnt += 1
    if x - 1 > 0 and y + 2 > 0:
        cnt += 1
    if x + 1 > 0 and y - 2 > 0:
        cnt += 1
    if x + 1 > 0 and y + 2 > 0:
        cnt += 1
    return cnt
print(kingKnight('a1'))
print(kingKnight('c2'))

def kingKnight_refactoring(S):
    x = ord(S[0]) - 96
    y = int(S[1])
    cnt = 0
    move =[[-2,-1],[-2,1],[2,-1],[2,1]]
    for m in move:
        if x + m[0] > 0 and y + m[1] > 0:
            cnt += 1
        if x + m[1] > 0 and y + m[0] > 0:
            cnt += 1
    return cnt
print(kingKnight_refactoring('a1'))
print(kingKnight_refactoring('c2'))

def kingKnight_dongbinna(S):
    x = ord(S[0]) - ord('a') + 1
    y = int(S[1])
    move =[(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
    cnt = 0
    for m in move:
        new_x = x + m[0]
        new_y = y + m[1]
        if new_x >= 1 and new_x <= 8 and new_y >= 1 and new_y <= 8:
            cnt += 1
    return cnt
print(kingKnight_dongbinna('a1'))
print(kingKnight_dongbinna('c2'))