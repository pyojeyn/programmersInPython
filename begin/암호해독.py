def solution(cipher, code):
    answer = ''
    i = code -1
    while i < len(cipher):
        answer += cipher[i]
        i += code
    return answer






# 슬라이싱 문법 사용
# [start:end:step]
# start : 슬라이싱을 시작할 인덱스(포함)
# end : 슬라이싱을 멈출 인덱스 (포함하지 않음). 생략하면 끝까지 가져옴
# step : 요소를 건너뛸 간격

str1 = 'abcdefghijklmnopqrs'
print(str1[1::3]) # behknq

def solution(cipher, code):
    return cipher[code-1::code]

print(solution("pfqallllabwaoclk", 2))


## range 사용
# range(시작, 끝, 간격)
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]

    return answer    

print(solution("pfqallllabwaoclk", 2))



for i in range(0, 10, 2):
    print(i)
