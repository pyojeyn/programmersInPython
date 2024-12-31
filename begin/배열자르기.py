def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

print(solution([1,2,3,4,5], 1, 3))
print(solution([1,3,5], 1, 2))



## 배열 슬라이싱
# list[start:end:step]
# start : 슬라이싱을 시작할 시작위치
# end : 슬라이싱을 끝낼 위치로 end는 포함 X (end전까지)
# step : 보폭. 몇개씩 끊어서 가져올지

exList = ['가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타', '파',
          '하', 'a', 'b', 'c', 'd', 'e', 
          'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p']


print(exList[2:]) # 2번자리부터 시작해서 끝까지
print(exList[-3:]) # ['n', 'o', 'p'] -> 마지막3번째부터 끝까지
print('-----------------------')
print(exList[:10]) # 0번부터 9번까지
print('-----------------------')
print(exList[3:7]) # 3번부터 6번까지 -> ['라', '마', '바', '사']