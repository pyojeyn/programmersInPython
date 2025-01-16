def solution(polynomial):
    answer = ''
    polynomial = polynomial.split()
    xInt = 0
    sInt = 0
    for i in range(len(polynomial)):
        if i % 2 == 0:
            if 'x' in polynomial[i]:
                if(len(polynomial[i]) == 1):
                    xInt += 1
                else:
                    xInt += int(polynomial[i][:-1])
            else:
                sInt += int(polynomial[i])

    if xInt > 0 and sInt > 0:
        if xInt == 1: # x의 계수가 1일때 그냥 x로 나타내는 처리
            answer = ' + '.join(['x', str(sInt)])
        else:
            answer = ' + '.join([str(xInt)+'x', str(sInt)])
    elif xInt > 0:
        if xInt == 1: # x의 계수가 1일때 그냥 x로 나타내는 처리
            answer = "x"
        else:    
            answer = str(xInt) + "x"
    else:
        answer = str(sInt)    
    return answer

print(solution("3x + 7 + x"))
print(solution("x"))
print(solution("8 + 8"))