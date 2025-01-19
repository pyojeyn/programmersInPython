def solution(common):
    isPlus = common[1] - common[0] == common[2] - common[1]
    answer = common[-1] + (common[1] - common[0]) if isPlus else common[-1] * (common[-1] // common[-2])
    return answer