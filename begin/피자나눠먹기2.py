def solution(n):
    answer = 0
    # 피자 6조각
    # n 은 피자 먹을 사람의 수
    # 남기지 않고 모두 같은 수의 피자 조각 먹어야함. 
    # 최소 몇판?
    # 10명, 5판 , 30
    for i in range(1, n+1):
        if (6 * i) % n ==0:
            answer = i
            break
    return answer


print(solution(4))