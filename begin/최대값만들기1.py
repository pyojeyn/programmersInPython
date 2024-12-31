def solution(numbers):
    sortedNumbers = sorted(numbers, reverse=True) 
    answer = sortedNumbers[0] * sortedNumbers[1]
    return answer



## 음수 인덱스 사용
# -1 : 마지막 요소
# -2 : 뒤에서 두번째 요소
# -3 : 뒤에서 세번째 요소
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]


# pop() 사용
def solution(numbers):
    numbers.sort()
    num1 = numbers.pop()
    num2 = numbers.pop()
    return num1 * num2




print(solution([1,2,3,4,5]))
print(solution([0, 31, 24, 10, 1, 9]))