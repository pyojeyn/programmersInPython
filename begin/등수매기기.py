def solution(score):
    
    # 각각 평균구해서 list 에 담습니다. 
    avgList = [sum(s) / 2 for s in score]

    # 다른 list 에 그 list 를 내림차순 sorted 해서 담고, 
    # rankAvg dict 에 key에 평균점수, value 에 등수를 담아줍니다.      
    sorted_avg = sorted(avgList, reverse=True)  # 정렬된 리스트 생성 
    rankAvg = {}
    rank = 0
    prev_score = None
    for index, score in enumerate(sorted_avg):
        # 그리디 알고리즘(Greedy Algorithm)
        if score != prev_score: # 점수가 다르면 새로운 등수
            rank = index + 1
        rankAvg[score] = rank
        prev_score = score
    
    # rankAvg = {value: index + 1 for index, value in enumerate(sAvgList)}
    # print("rankAvg= ", rankAvg)

    # 먼저 구한 list 에서 dict 에서 찾습니다. 
    return [rankAvg[a] for a in avgList] 

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))