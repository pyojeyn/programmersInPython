def solution(num_list):
    answer = []
    lenOfNumList = len(num_list)

    indexOfNumList = lenOfNumList - 1
    for n in range(0, lenOfNumList):
        answer.append(num_list[indexOfNumList])
        indexOfNumList-= 1

    return answer



## while 문 사용
my_list = [1, 2, 3]
while my_list:  # 리스트가 비어 있지 않으면 반복
    print(my_list.pop())  # 리스트의 마지막 요소를 제거하고 출력


## 적용
def solution2(numlist):
    result = []
    while(numlist):
        result.append(numlist.pop())
    return result

print(solution2([2,3,4,5,6]))


print('--------------------------------')

## reverse() 사용
def solution3(num_list):
    num_list.reverse()
    return num_list

print(solution3([2,3,4,5,6]))
