# https://www.acmicpc.net/problem/10828
# deque안써도 되지만 익숙해지기 위해 써보자.
import sys
from collections import deque

n = sys.stdin.readline().rstrip() # 시간초과를 방지하기 위해서 input 대신 사용한다.
stack = deque()

for i in range(int(n)): # 명령어 횟수만큼 반복
    com = sys.stdin.readline().split() # 명령어 입력받기
    if len(com) == 2: # 명령어 2개면 push 
        stack.append(int(com[1])) 
    elif len(com) == 1: # 나머지
        if com[0] == 'top': 
            if len(stack) == 0: 
                print(-1)
            else:
                print(stack[-1])
        elif com[0] == 'pop':
            if len(stack) == 0: 
                print(-1)
            else:
                print(stack[-1])
                stack.pop()
        elif com[0] == 'size':
            print(len(stack))
            
        elif com[0] == 'empty':
            if len(stack) == 0:
                 print(1)
            else:
                 print(0)
        elif com[0] == 'top':
            if len(stack) == 0:
                 print(-1)
            else:
                 print(stack[-1])
    else:
        continue
