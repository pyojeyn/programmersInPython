def solution(array, height):
    return len([h for h in array if h > height])


## list 안쓰고 sum() 활용
def solution(array, height):
    return sum(1 for h in array if h > height)