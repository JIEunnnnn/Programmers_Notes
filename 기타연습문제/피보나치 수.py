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
    
