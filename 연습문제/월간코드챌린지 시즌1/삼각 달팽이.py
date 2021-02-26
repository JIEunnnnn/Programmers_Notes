#월간코드챌린지 시즌1 삼각달팽이.py
#반시계방향으로 숫자대입하여, 리스트 출력하는 문제
#
#고려사항 
# 1. N값에 따라 바뀌는 방향갯수 파악가능(4개일경우 4번방향 바뀜)
# 2. 바뀔때마다 채워야하는 숫자 줄어드는 규칙 이해해야함

def solution(n):
    answer = []
    
    tr_list = [[0]*j for j in range(1,n+1)]
    #print(tr_list)
                
    row = -1
    col = 0
    num = 1
    
    # N=6 => 6 + 5 + 4 + 3 + 2 + 1
    
    for i in range(n) : #N까지 for문돌리기
        for j in range(i, n) : #방향 바뀔때마다 채워야하는 숫자 한개씩 줄어듬!!(숫자갯수)

            
            if i % 3 == 0 :
                row+=1 
            
            elif i % 3 == 1:
                col += 1
                
    
            elif i % 3 == 2:
                row -= 1
                col -= 1       
                
            
            tr_list[row][col] = num
            num+=1
            #print(tr_list)
            
    for i in tr_list :
        answer.extend(i)
    
    return answer
