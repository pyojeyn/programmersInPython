def solution(my_string):
    answer = ''
    myStringList = list(my_string)
    slist = []
    for s in myStringList:
        if s.islower():
            slist.append(s.upper())
        else:
            slist.append(s.lower())    
            
    answer = ''.join(slist)        
    return answer




print(solution('cccCCC'))
