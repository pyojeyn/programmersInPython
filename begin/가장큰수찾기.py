def solution(array):
    tmpArr = sorted(array, reverse=True)    
    return [tmpArr[0], array.index(tmpArr[0])]


# max 함수 사용
def solution(array):
    maxNum =  max(array)
    return [maxNum, array.index(maxNum)]

print(solution([1,5,4]))