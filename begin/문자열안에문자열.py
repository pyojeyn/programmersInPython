def solution(str1, str2):
    return 1 if str2 in str1 else 2

# 문자열 포함 유무 확인. 
# in, not in, find

print(solution("ppprrrogrammers", "pppp"))



apple = 'apples'

print(apple.find('tt'))
#  find 문자열은 단순히 포함 유무만 확인할 수 있을 뿐만이 아니라 
# 문자열의 어느 index에 포함되어 있는지까지 확인이 가능
# 없으면 -1리턴