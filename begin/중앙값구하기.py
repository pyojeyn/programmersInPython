def solution(array):
    array.sort()
    return array[int(len(array) / 2)]


print(solution([9,-1,0]))