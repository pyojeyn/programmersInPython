def solution(n):
    # set 하나 초기화
    soinsuSet = set()

    # sosu 2부터 시작하기때문에 2로 초기화
    sosu = 2

    # n 1이 될때까지 반복
    while n!=1:
        # n에서 sosu 나눈 나머지값이 0 이면 sosu 값 추가
        if(n % sosu == 0):
            soinsuSet.add(sosu)
            n //= sosu
        # 나머지값 0 아니면 소수값 1 증가시켜줘서 반복.    
        else:
            sosu += 1

    # 문제 중 오름차순으로 담은 배열을 return하도록이 있다. 
    # [2, 3] or [3, 2] 순서가 랜덤으로 바뀔 수 있기때문에 sorted 해주어야 함.
    return sorted(list(soinsuSet))

print(solution(17))