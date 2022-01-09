# TC 5 -> 11475
# 3, 30, 33, 31 등
# 즉, %10 3 이거나 /10 한것의 몫이 3이거나
# 00시 00분 00초 부터 N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수 출력
def checkTF(N):
    if N % 10 == 3 or N / 10 == 3:
        return True
    return False

def trackingThree(N):
    hour = 0
    min = 0
    sec = 0
    result = 0
    for i in range(N*60*60+3599):
        sec += 1
        if sec == 60:
            min += 1
            sec = 0
        if min == 60:
            hour += 1
            min = 0
        if checkTF(sec) or checkTF(min) or checkTF(hour):
            result += 1
    return result
print(trackingThree(5))

def trackingThree_dongbinna(N):
    cnt = 0
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    cnt+=1
    return(cnt)
print(trackingThree_dongbinna(5))


