def solution(num_list):    
    짝, 홀 = sum(1 for i in num_list if i % 2 == 0), sum(1 for i in num_list if i % 2 == 1)
    return [짝, 홀]