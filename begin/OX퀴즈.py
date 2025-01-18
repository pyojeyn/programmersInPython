def solution(quiz):
    answer = []
    
    for q in quiz:
        qList = q.split()        
        result = int(qList[0]) + int(qList[2]) if qList[1] == '+' else int(qList[0]) - int(qList[2])
        answer.append('O') if result == int(qList[4]) else answer.append('X')    
    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
print(solution(["3 - 4 = -1", "5 + 6 = 11"]))