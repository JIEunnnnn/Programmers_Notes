#2019 카카오 개발자 겨울 인턴십. 크레인 인형뽑기 게임
#인형이 몇개 사라지는지 구현하는 알고리즘
#
#처음 문제길이보고 당황, BUT 스택구현임을 깨닫..! 
#테케 1,2 번 에러 뜨는것 보고 stack 처음에 0 넣은게 문제였다는걸 알게됨 
#크레인이 빈곳에 가서, 인형을 안가져왔을경우 리스트오버 발생...!!  ==> ex) 0 == 0 일경우

def solution(board, moves):
    answer = 0
    
    stack = [] 
    size = len(board)
    for i in moves :
        i = i -1
        for j in range(size) :
            
            if board[j][i] != 0 :
                stack.append(board[j][i])
                board[j][i] = 0
                break 
        
        #print("테스트")
        #print(stack)
        
        if len(stack) >= 2 :
            if stack[-1] == stack[-2] :
                stack.pop()
                stack.pop()
                answer +=2
        
    
    return answer
  
================================================
 
#1차시도 => 테케1,2 에러
  def solution(board, moves):
    answer = 0
    
    stack = [0,] 
    size = len(board)
    for i in moves :
        i = i -1
        for j in range(size) :
            
            if board[j][i] != 0 :
                stack.append(board[j][i])
                board[j][i] = 0
                break 
        
        #print("테스트")
        #print(stack)
        
        if stack[-1] == stack[-2] :
            stack.pop()
            stack.pop()
            answer +=2
        
              
    return answer
