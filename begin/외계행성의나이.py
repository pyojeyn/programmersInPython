def solution(age):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
 
    return ''.join([alphabet[int(s)] for s in str(age)])    

print(solution(100))

