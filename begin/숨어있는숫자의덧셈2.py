import re

def solution(my_string):
    removeNumStr = re.sub(r'[a-zA-Z]+', ' ', my_string)
    removeNumStrList = removeNumStr.split()
    answer = sum(int(n) for n in removeNumStrList)
    return answer


print(solution("1a2b3c4d123Z"))