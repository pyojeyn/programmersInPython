def solution(my_string):
    strArr = my_string.split()

    answer = int(strArr[0])
    operator = ''
    for i in range(1, len(strArr)):
        if i % 2 != 0:
            operator = strArr[i]
        else:       
            if operator == "+":
                answer += int(strArr[i])
            else:
                answer -= int(strArr[i])
    return answer


print(solution("2 - 4 + 4 + 3"))

st3 = -6
print(int(st3))