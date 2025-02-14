def solution(bin1, bin2):
    tmpResult = int(bin1, 2) + int(bin2, 2)
    return str(bin(tmpResult)[2:])

solution("10", "11")