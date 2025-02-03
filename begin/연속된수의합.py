def solution(num, total):
    sumNum = sum(range(num))
    # n 을 구해라! 시작 숫자를 구함.
    n = int((total - sumNum) / num)
    # 연속된 수만큼 for 반복, 시작숫자에 0부터 증가하는 i를 더해주어서 list 만듬
    return [n + i for i in range(num)]    

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))