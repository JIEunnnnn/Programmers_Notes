#LV.1 약수의 합
#주어진 정수에서 약수의 합구하기 
#
#for문 및 %연산 활용
#

def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        if n % i == 0 :
            answer += i 
    
    return answer
  
  
