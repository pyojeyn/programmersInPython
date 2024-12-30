def solution(numbers):
    lenOfNumbers = len(numbers)
    sum = 0
    while(numbers):
        sum += numbers.pop()
    result = sum / lenOfNumbers
    return result


## sum() 을 사용 : 파이썬의 내장함수
def solution(numbers):
    return sum(numbers) / len(numbers)


## 그냥 평범한 for문 
def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    answer = sum / len(numbers)
    return answer


print(solution([1,2,3,4,5,6,7,8,9,10]))