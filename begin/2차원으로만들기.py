def solution(num_list, n):
    answer = []
    size = int(len(num_list) / n)
    for _ in range(size):
        answer.append(num_list[:n])
        del num_list[:n]
        
    return answer

## 대안
def solution2(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]

# range(0, len(num_list), n)
# n 간격으로 인덱스 생성

# range(start, stop, step)
for i in range(0, 9, 3):
    print('i: ', i) # 0, 3, 6
    print('i+n: ', i + 3)


print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948, 1000, 299, 300], 4))