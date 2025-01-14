def solution(balls, share):

    nfac = factorial(balls)
    mfac = factorial(share)
    nMinusM = factorial(balls - share)

    return nfac / (nMinusM * mfac)

def factorial(num):
    result = 1
    for n in range(1, num+1):
        result *= n
    return result