def solution(a, b):
    answer = 0
    # 1. a와b의 최대공약수 구한다. 
    gcd = getGcd(a, b)

    # 2. b를 최대공약수로 나눈다. 
    b //= gcd

    # 3. 최대공약수로 나눈 b의 값을 소인수분해 한다. 
    soinsuList = getSoinsu(b)

    count = len(set(filter(lambda x: x != 2 and x != 5, soinsuList)))
    print("count", count)
    
    return 2 if count > 0 else 1

def getGcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
def getSoinsu(b):
    results = set()
    sosu = 2
    while b > 1:
        if b % sosu == 0:   
            results.add(sosu)
            b //= sosu
        else:
            sosu+=1
    return results


print(solution(11, 22))
