import sys

s = sys.stdin.readline().rstrip()
l1 = list(s)
sl = []
nl = []
n = 0
for i in l1:
    if 65 <= int(ord(i)) <= 90:
        sl.append(i)
    elif 49 <= int(ord(i)) <= 57:
        n = n + int(i)
    else:
        continue
sl = sorted(sl)
sl.append(str(n))
print(''.join(sl))
