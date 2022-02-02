from sys import stdin

def gcd(a,b):
    if a % b == 0: return b
    return gcd(b, a % b)
t = int(stdin.readline().rstrip())
lst = [list(map(int, stdin.readline().split())) for _ in range(t)]
[print((a * b) //gcd(a,b)) for a,b in lst]
