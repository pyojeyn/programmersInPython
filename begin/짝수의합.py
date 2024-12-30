def solution(n):
    answer = 0
    for num in range(0, n+1):
        if num % 2 == 0:
            answer += num
    return answer



# 0 ~ 9 까지 출력.
# 첫번째 인자 ~ 마지막인자-1
for s in range(0, 10):
    print("s : ", s)