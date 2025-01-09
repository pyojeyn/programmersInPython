def solution(array):
    return sum(s.count('7') for s in [str(a) for a in array])    

print(solution([7, 77, 17]))



sList = [7, 77, 17]
print(len(str(sList)))