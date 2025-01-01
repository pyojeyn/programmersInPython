def solution(hp):
    answer = 0
    if hp // 5 > 0:
        answer += hp // 5
        lefted = hp % 5
        
        if lefted // 3 > 0:
            answer += lefted // 3
            lefted = lefted % 3
            answer += lefted
            
        else:
            answer += lefted  
            
    elif hp // 3 > 0:
        answer += hp // 3
        lefted = hp % 3
        answer += lefted
    else:
        answer += hp             

    return answer


print("result: ",solution(999))


print('---------------------------------------')


# hp 를 줄여나가면 되는거였....
def solution(hp):
    answer = 0
    answer += hp//5
    hp %= 5
    
    answer += hp//3
    hp %= 3
    
    answer += hp//1
    return answer

print("result: ",solution(24))
