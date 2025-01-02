def solution(number):
    sortedNumberList = sorted(number)
    minusMax = sortedNumberList[-1] * sortedNumberList[-2]
    plusMax = sortedNumberList[0] * sortedNumberList[1]
    
    return max(minusMax, plusMax)


print(solution([10, 20, 30, 5, 5, 20, 5]))