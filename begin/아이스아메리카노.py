def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer




print(solution(15000))
print(15000 // 5500) # 사먹을 수 있는 개수
print(15000 % 5500) # 잔돈 