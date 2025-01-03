# list 의 더하기 연산으로 해결
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


print(solution([1, 2, 3], 'right'))
print(solution([4, 455, 6, 4, -1, 45, 6], 'left'))         