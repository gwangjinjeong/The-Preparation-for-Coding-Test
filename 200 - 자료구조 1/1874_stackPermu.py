from itertools import permutations
import math
import sys
# 12345678 씩 순서대로 push 된 stack에서 43687521가 출력되게 하려면 
# 어떤 순서로 push pop해야 43687521가 나오는지에 대한 문제

input = sys.stdin.readline
n = input()
x = [i for i in range(1,int(n)+1,1)]
print(x)
