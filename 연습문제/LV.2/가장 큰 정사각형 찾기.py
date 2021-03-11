#LV.2 가장 큰 정사각형찾기
#주어진 행렬에서 가장 큰 정사각형 찾는문제
#
#땅따먹기 문제랑 유사하게 차례대로 더함으로써, 해결하는 문제^_^ ㅠ
#DP 문제는 아직 매우매우 어려운거같다...

#Dynamic Programming 
def solution(board):
    max_point = 0
    for i in range(len(board)) : #전체가 0 인경우 
        max_point += sum(board[i][:])
    if max_point == 0 :
        return 0
    elif max_point == 1 : #[1,0],[0,0] => 1
        return 1
    max_point = 0
    for i in range(1, len(board)) : #첫번째 행X 
        for j in range(1, len(board[0])) : #첫번째 열X
            if board[i][j] == 0 :
                continue 
            else :
                min_point = min(board[i][j-1], board[i-1][j], board[i-1][j-1])
                min_point +=1 
                board[i][j] = min_point 
                if max_point < board[i][j] :
                    max_point = board[i][j]
    
    return max_point ** 2

#1차시도 
def solution(board):
    answer = 1234
    width = [0 for i in range(len(board[len(board)-1]))]
    print(width)
    
    for i in range(len(board)) :
        for j in range(len(width)) :
            width[j] += board[i][j]
            
        print(width)
    
    #for i in board :
            
    
    

    return answer
