# 두개의 비열을 비교할대는 in 연산자를 사용.
# 

def solution(s1, s2):
    list = [i for i in s1 if i in s2]
    return len(list)


print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"],["m", "dot"]))


## 리스트에서 같은 값 찾기 
# 1. set(s1)&set(s2) -> & 교집합.
# 2. [i for i in A if i in B] -> Comprehension
# 3. intersection() 메서드 -> set(s1).intersection(set(s2)) 
#       -> s1과 s2 두 집합에서 공통된 원소만을 포함한 새로운 집합 반환.
