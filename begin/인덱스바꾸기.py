def solution(my_string, num1, num2):
    answer = ''
    for i in range(len(my_string)):
        if i == num1:
            answer += my_string[num2]
            continue
        if i == num2:
            answer += my_string[num1]
            continue
        answer += my_string[i]  
    return answer
        

## swap , 튜플 언패킹 활용
def solution(my_string, num1, num2):
    # 문자열 -> 리스트르 변환(문자열은 변경할 수 없는 immutable객체이지만, 
    # list 는 변경 가능한 mutable 객체라서 특정 위치의 값을 수정하거나 교환할 수 있다.)
    sList = list(my_string) 

    # 리스트의 num1번째 요소와 num2 번째 요소를 교환.
    # 파이썬에서는 두 값을 스왑할 때 임시 변수를 만들 필요 없음.
    sList[num1], sList[num2] = sList[num2], sList[num1]
    return ''.join(sList)



print(solution("hello", 1, 2))        



