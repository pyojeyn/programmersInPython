def solution(before, after):
    beforeList = sorted(list(before))
    afterList = sorted(list(after))
    ifEqual = beforeList == afterList

    return 1 if ifEqual else 0


print(solution("olleh", 'hello'))
print(solution("allpe", 'apple'))


str3 = "apple"
print(sorted(str3))