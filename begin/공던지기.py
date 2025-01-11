# 배열 순환할때 나머지 연산으로 나온 값이 인덱스 값이 된다.

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))