def solution(array, n):
    array.sort()
    answer = array[0]
    diff = abs(array[0] - n)
   
    for i in range(1, len(array)):
        tmpDiff = abs(array[i] - n)
        
        ## 오름차순으로 정렬이된 배열이기 때문에
        # answer는 작은 값으로 이미 설정된 상태라 추가 작업이 필요하지 않다.
        if(tmpDiff < diff):
            diff = tmpDiff
            answer = array[i]

    return answer


print(solution([10, 12, 13, 15], 12))