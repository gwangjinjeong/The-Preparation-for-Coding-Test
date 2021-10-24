# 1로 만들기(p217)
# 정수 X가 주어졌을때 가능 연산 4가지
# /5 = 0 -> 5
# /3 = 0 -> 3
# /2 = 0 -> 2
# X-1
# TC 26 => 25(-1) => 5(/5) => 1(/5)
# TC
# 연산을 사용하는 횟수의 최솟값을 출력하라.
# ai = min(ai-1, a/2, ai/3, ai/5) + 1
# f(0) f(1) f(2) f(3)
def get1(Xn,cnt,dp):
    if Xn == 1:
        return dp.append(cnt)
    else:
        cnt = cnt + 1
        if Xn % 5 == 0:
            Xn = Xn / 5
            get1(Xn, cnt,dp)
        if Xn % 3 == 0:
            Xn = Xn / 3
            get1(Xn, cnt,dp)
        if Xn % 2 == 0:
            Xn = Xn / 2
            get1(Xn, cnt,dp)
        if Xn - 1 != 1:
            Xn = Xn - 1
            get1(Xn, cnt,dp)



X = int(input())
dp = []
cnt = 0 # 처음부터 3으로 나눠지거나
dps = get1(X,cnt,dp)
print(dps)
print(min(int(dps)))
