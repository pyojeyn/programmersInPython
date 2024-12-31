def solution(my_string):
    myStringList = list(my_string) # list 로 변경
    myStringList.reverse() # 뒤집기
    my_string = ''.join(myStringList) # 다시 string 으로 변경
    return my_string




# list[::-1] 사용 -> 원래 리스트를 뒤집은 새로운 리스트를 반환한다.
def solution(my_string):
    return my_string[::-1]



# reversed() 사용
def solution(my_string):
    return ''.join(reversed(my_string))

print(solution("jaron"))
print(solution("bread"))

str1 = reversed('hello')
print(''.join(str1))


