import sys
si = sys.stdin.readline
a, b = list(map(int, si().split()))
def gcd(a, b):
    if a % b == 1: return 1
    if a % b == 0: return b
    return gcd(b, a % b)
gcd = gcd(a, b)
lcm = (a * b) // gcd
print(gcd)
print(lcm)