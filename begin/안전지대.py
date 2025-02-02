def solution(board):

    # 위험지대 표시할 새로운 배열
    newBoard = [[0 for _ in range(len(board))] for _ in range(len(board))]

    # 지뢰 지역 찾기
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 1:
                danger(i, j, newBoard)
    
    return sum([nb.count(0) for nb in newBoard])

def danger(i, j , newBoard):
    overX = len(newBoard)
    overY = len(newBoard[0])

    newBoard[i][j] = 1
    if i > 0:
        newBoard[i-1][j] = 1
    if i < overX - 1:
        newBoard[i+1][j] = 1
    if j < overY - 1:
        newBoard[i][j + 1] = 1
    if j > 0 :
        newBoard[i][j-1] = 1
    if i > 0 and j > 0:
        newBoard[i-1][j-1] = 1
    if i < overX -1 and j > 0:
        newBoard[i + 1][j - 1] = 1
    if i > 0 and j <overY -1:
        newBoard[i -1][j + 1] = 1
    if i < overX -1 and j < overY -1:
        newBoard[i + 1][j + 1] = 1  
    

# BFS(너비 우선 탐색) or DFS(깊이 우선 탐색)


####################
# 2차원 배열은 그냥 표라고 생각하기. 
#   - 행(i) 는 세로방향 (위아래)
#   - 열(j) 는 가로방향 (좌우)
#   - (i, j)  , (위아래, 좌우)




def solution2(board):
    lenOfBoard = len(board) # 보드의 크기
    danger_board = [[0] * lenOfBoard for _ in range(lenOfBoard)]  # 위험 지역 표시를 위한 배열 초기화


    # 지뢰 주변 위험 지역 표시 방향 
    directions = [
        (-1, -1), (-1, 0), (-1, 1), # 위/왼쪽 대각선쪽, 위쪽, 위/오른쪽 대각선
        (0, -1),           (0, 1),  # 왼쪽, # 오른쪽,
        (1, -1),  (1, 0),   (1, 1)  # 아래/왼쪽 대각선쪽, 아래쪽, 아래/오른쪽 대각선
    ]

    for i in range(lenOfBoard):
        for j in range(lenOfBoard):
            if board[i][j] == 1: # 지뢰가 있는 경우
                danger_board[i][j] = 1 # 위험지역에 지뢰위치도 1이라고 표시 
                for dx, dy in directions: # 각각 방향키 조회 해서 지뢰위치 x축, y축 위치에 더해줘서 위험지역 추출
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < lenOfBoard and 0 <= ny < lenOfBoard: # 보드 범위 안에 있는지 확인
                        danger_board[nx][ny] = 1
                
    return sum([nb.count(0) for nb in danger_board])

print(solution2([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
# print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))