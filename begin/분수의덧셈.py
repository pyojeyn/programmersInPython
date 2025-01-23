def solution(numer1, denom1, numer2, denom2):
    # 둘중의 큰 분모가 최소공배수인지 확인하기 
    isdenom = max(denom1, denom2) % min(denom1, denom2) == 0
    
    # 임시 분모 구하기
    tmpDenom = max(denom1, denom2) if isdenom else denom1 * denom2
    
    # 임시 분자 구하기
    tempNumer = (tmpDenom // denom1) * numer1 + (tmpDenom // denom2) * numer2
    
    # 분자, 분모의 최대공약수  구하기
    gcd = getGCD(tmpDenom, tempNumer)
    
    return [tempNumer // gcd, tmpDenom // gcd]


def getGCD(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(solution(1,2,3,4))
print(solution(9,2,1,3))
