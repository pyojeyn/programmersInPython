def solution(sides):

    # [11, 7] 일때 
    # 가장 긴게 11일경우 : 5 부터 시작 (7 + 5 = 12) 가장 긴변보다 크니까 
    # 가장 긴게 나머지 하나일 경우 : 18 보다 작아야 된다. (11+7)
    start = max(sides) - min(sides) + 1
    end = sum(sides)
    return len(range(start, end))

print(solution([11,7]))
print(solution([1,2]))
print(solution([3,6]))