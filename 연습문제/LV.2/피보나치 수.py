#LV.2 피보나치 수
#피보나치 수의 /1234567 나머지값구하기
#
#처음 재귀함수(top-down)로 풀었을때는 시간초과발생 => for문으로 0,1 하나씩 더하는 알고리즘(bottom-up)으로 수정 
#

def solution(n):
    zero = 0
    one = 1 
    
    for i in range(2,n+1) :
        zero, one = one, zero+one 
    
    return one % 1234567

=======================================================
#1차시도
#정확성,..42.9..(런타임에러ㅏ...시간초과...)

def F(i) :
    if i == 0 :
        return 0 
    elif i == 1 :
        return 1
    else :
        return F(i-1) + F(i-2)

def solution(n):
    
    answer = F(n) % 1234567
    return answer
    
