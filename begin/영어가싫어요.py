def solution(numbers):
    answer = ""
    numStrList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    tmp = ""
    for n in numbers:
        tmp += n
        if(tmp in numStrList):
            answer += str(numStrList.index(tmp))
            tmp = ""
    return int(answer)


print(solution("onetwothreefourfivesixseveneightnine"))