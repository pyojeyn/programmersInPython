def solution(id_pw, db):
    answer = 'fail'
    loginId, loginPw = id_pw[0] , id_pw[1]

    for d in db:
        if loginId in d:
            if loginPw in d:
                answer = 'login'
            else:
                answer = 'wrong pw'
    return answer


print(solution(["rabbit04", "98761"], 
               [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))

arr2 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

# 2차원 배열 
# 각 하위 리스트에서 첫 번째 값은 i, 두 번째 값은 p로 할당
# 리스트 언패킹임
for i, p in arr2:
    print("i는 뭐야 ? ", i) # jaja11
    print("p는 뭐야 ? ", p) # 98761

for a in arr2:
    print("a는? ", a) # ['jaja11', '98761']


# 언패킹
arr3 = ['apple', 'banana']

a, b = arr3

print("a : ", a)
print("b : ", b)