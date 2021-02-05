


=========================================
#1차시도
#정확성 88....

def solution(n,a,b):
    answer = 1

    while True :
        if a+1==b or b+1==a :
            return answer
        
        answer +=1
        
        if a%2 == 0 :
            a = a/2
        else :
            a = (a+1)/2
        
        if b%2 == 0 :
            b = b/2
        else :
            b = (b+1)/2
       
