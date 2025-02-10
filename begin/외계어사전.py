def solution(spell, dic):
    answer = 2

    sortedSpell = ''.join(sorted(spell))
    for d in dic:
        sortedD = ''.join(sorted(d))
        if sortedSpell == sortedD:
            answer = 1
    return answer


print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))