# TC 02984 -> 576
# 567 -> 210
# 12 면 곱하기 보다는 덧셈이 낫다.
# 즉, 0 혹은 1이면 덧셈이 낫다.
# 1개만 들어오면 걍 반환
def multiOrPlus(s):
    tmp = list(map(lambda x: int(x), list(str(s))))
    result = tmp[0]
    if len(tmp) == 1:
        return result
    else:
        for cur in range(1, len(tmp)):
            if result ==0 or result == 1 or tmp[cur] == 0 or tmp[cur] == 1:
                result = result + tmp[cur]
            else:
                result = result * tmp[cur]
    return result

print(multiOrPlus('567'))

def multiOrPlus_dongbinna(s):
    tmp = list(map(lambda x: int(x), list(str(s))))
    result = tmp[0]
    for cur in range(1, len(tmp)):
        if result <=1 or tmp[cur]<=1:
            result += tmp[cur]
        else:
            result *= tmp[cur]
    return result

print(multiOrPlus('567'))
