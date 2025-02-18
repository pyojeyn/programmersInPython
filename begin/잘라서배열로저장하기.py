def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]    

print(solution('abcdef123', 3))
print(solution('abc1Addfggg4556b', 6))

# 슬라이싱은 초과해도 에러 안남
numList = ['a', 'b', 'cc', 'dd', 'e', '6']
print(numList[3:10])