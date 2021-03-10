#LV.2 가장 큰 정사각형찾기
#
#
#
#

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
