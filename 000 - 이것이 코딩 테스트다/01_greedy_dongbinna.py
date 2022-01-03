# 그리디 문제: 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 한다.

# TC N=17 K=4 => 3
# 17 -> 16 -> 4 -> 1
# 25 -> 5 -> 1
def untilBeOne(N, K):
    cnt = 0
    while(N!=1):
        if N % K == 0:
            N = N / K
            cnt = cnt + 1
        else:
            N = N -1
            cnt = cnt + 1
    return cnt
print(untilBeOne(3,4)) #위는 한번 반복할때마다 반복횟수마다 기하급수적으로 올라간다.

def untilBeOne_dongbinna(N, K): # 동빈나는 코드가 좀 빨리 실행될 수 있도록 테크닉을 가미하였다.
    result = 0
    while(N!=1):
        temp = (N // K) * K
        result += (N - temp)
        if N < K:
            break
        result += 1
        N //= K

    result +=(n - 1)
    return result

print(untilBeOne_dongbinna(3,4))
