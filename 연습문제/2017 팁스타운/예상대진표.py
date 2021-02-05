#2017팁스타운 예상대진표
#a와 b가 몇번째 경기에서 만나는가?
#
#a=4, b=5일경우를 고려안해서... 실패했으며 올림활용하여 코드수정 
#

import math

def solution(n,a,b):
    answer = 1

    while True :
        if math.ceil(a/2) == math.ceil(b/2) :
            return answer
        
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)

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
       
