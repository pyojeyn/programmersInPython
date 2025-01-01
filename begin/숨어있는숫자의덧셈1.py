import re

# 정규식
def solution(my_string):
    pattern = r"\d"
    matches = re.findall(pattern, my_string)
    numList = [int(i) for i in matches]
    return sum(numList)


# isdigit() 사용하기.
def solution1(my_string):
    print("isdigit() 사용하기.")
    answer = sum(int(i) for i in my_string if i.isdigit())
    return answer


def solution2(my_string):
    answer = 0
    strList = list(my_string) # list로 형변환
    for i in strList: # list 순회
        if i.isdigit(): # 숫자인지 판별
            answer += int(i) # int로 형변환하여 더함
        else:
            continue
    return answer       

print(solution2("1a2b3c4d123"))