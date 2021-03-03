#LV.1 x만큼 간격이 있는 n개의 숫자
#정수X의 배수가 N개만큼 존재하는 리스트 구현  
#
#x=0일경우도 생각하자...!! 젭알..ㅠㅠ 
#

def solution(x, n):
    answer = []
    
    
    
    if x > 0 :
        for i in range(x,x*n+1,x) :
            answer.append(i)
    elif x< 0 :
        for i in range(x,x*n-1, x) :
            answer.append(i)
    else : #x=0
        for i in range(n) :
            answer.append(x)
    
    return answer
