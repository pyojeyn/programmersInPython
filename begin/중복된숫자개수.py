def solution(array, n):
    list = [i for i in array if i==n]
    return len(list)





# count() 로도 가능하다.
# 리스트나 튜플 등에서 사용. 주어진 값이 리스트 내에서 몇 번 등장하는지 세는 함수.

def solution(array, n):
    return array.count(n)


print(solution([0, 2, 3, 4], 0))