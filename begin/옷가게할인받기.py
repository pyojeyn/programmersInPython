def solution(price):
    more10 = 0.05
    more30 = 0.1
    more50 = 0.2
    answer = 0

    if price >= 500000:
        price -= price * more50
    elif price >= 300000:
        price -= price * more30     
    elif price >= 100000:
        price -= price * more10      

    answer = int(price)
    
    return answer            


print(solution(580000))
print(solution(700000))