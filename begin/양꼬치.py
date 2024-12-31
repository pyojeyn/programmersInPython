def solution(n, k):
    serviceDrink = n // 10
    양꼬치 = 12000
    음료수 = 2000
    return (양꼬치 * n) + ((k-serviceDrink) * 음료수) 


print(solution(64,6))