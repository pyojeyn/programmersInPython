def solution(n):
    answer = 0

    for i in range(1, n+1):
        if(i * i > n):
            break

        if(n % i == 0):
            if i * i == n:
                answer += 1
            else:
                answer += 2
    return answer

## 이건 좀 헷갈렸다...ㅋ


print(solution(100))