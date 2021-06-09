#LV.3 2 x n 타일링
#타일을 가로로, 세로로 배치하는 경우의 수 구하기
#
#뭔가 풀기힘들다 = 점화식으로 생각하자!! 
#

def solution(n):
    answer = 0
    first, second = 1, 2 
    for i in range(3,n+1) :
        fir, sec = second , first+second
        first, second = fir, sec
    
    #print(second)
        
    
    
    return second%1000000007
