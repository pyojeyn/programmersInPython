def solution(n):
    answer = 2
    # if n == 1:
    #     return 1
    for i in range(1, n+1):
        if n % i == 0:
            result = n // i
            if i == result:
                answer = 1
    return answer


print(solution(1))


# 0.5 를 제곱하여 제곱근을 구하고 정수인지 아닌지에 따라 판단하기.
def solution(n):
    return 1 if(n ** 0.5) % 1 == 0 else 2


# 파이썬에서의 삼항 연산자
# result = 참일때의 값 if 조건 else 거짓일때의 값.
result = '맞아' if 1>1 else '틀려'
print('result= ', result)


print(solution(1))
