# 출처: https://www.acmicpc.net/source/34111610
import sys
def check(s):
  for i in range(int(len(s)/2)):
    s = s.replace("()","")
  if s == "":
    return "YES"
  else:
    return "NO"
for i in range(int(input())):
  print(check(sys.stdin.readline().strip()))