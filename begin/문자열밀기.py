def solution(A, B):
    if A == B:
        return 0
    
    for i in range(1, len(A)+1):
        A = A[-1] + A[:-1]
        if B == A:
            return i

    return -1

print(solution("hello", "llohe"))