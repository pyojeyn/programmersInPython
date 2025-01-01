def solution(rsp):
    # 가위 2, 바위 0 , 보 5
    answer = ''

    sizeOfLen = len(rsp)
    
    for i in range(sizeOfLen):
        if rsp[i] == '2':
            answer += '0'
        elif rsp[i] == '0':
            answer += '5'
        else:
            answer += '2'        
    return answer



print(solution("205"))