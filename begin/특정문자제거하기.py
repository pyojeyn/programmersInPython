def solution(my_string, letter): 
    return ''.join([s for s in my_string if s != letter])



## 파이썬에도 replace 가 있음 ~! 
def solution(my_string, letter):
    return my_string.replace(letter, '')

print(solution("BCBdbe", "B"))