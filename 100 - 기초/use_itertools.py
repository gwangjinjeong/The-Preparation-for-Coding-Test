from itertools import permutations, combinations, product
from itertools import combinations_with_replacement as cwr

data = ['A','B','C']
permu = list(permutations(data, 2)) # 모든 순열 일렬로 나열
comb = list(combinations(data,2)) # 모든 조합 구하기

prod = list(product(data, repeat=2)) # (중복을 포함한) 모든 순열 구하기
comWrepl = list(cwr(data, 2)) # (중복을 포함한) 모든 조합 구하기
print(f'data = {data}')
print(f'permuation = {permu}\n\
combinations = {comb} \n\
permuation allowed duplication = {prod} \n\
combination allowed duplication = {comWrepl} \n')
