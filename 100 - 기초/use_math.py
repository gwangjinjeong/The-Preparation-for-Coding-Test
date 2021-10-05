import math

def lcm(a,b):
    gcd = math.gcd(a,b)
    result = gcd * a//gcd * b//gcd
    return result

print(math.factorial(5)) # 팩토리얼

print(math.sqrt(7)) # 루트

print(math.gcd(14,21)) # 최대공약수

print(lcm(14,21)) # 최소공배수

print(math.pow(7,2)) # 제곱근