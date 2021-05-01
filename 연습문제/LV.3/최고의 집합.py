#LV.3 최고의집합
#S의 합을 유지하며, 곱이 최대인 집합을 구하는 문제 
#
#중간값들을 곱하는것이 가장 큰 값임을 알수있었으며
#숫자에 대해 중복허용 및 나머지 처리하는 과정이 관건이었다!!

def solution(n, s):
    answer = []
    #N개의 자연수의 합이 S가 되는 집합 
    #곱이 최대여야 함..! => 중간값들을 곱하는 것이.. 최댓값..!
     
    tmp = s // n 
    others = s % n
    
    
    if others == 0 : #나눠지는 경우
        return [tmp] * n     
        
    else :
        if tmp == 0 :
            return [-1] 
        
        else :
            # N = 5, S = 27 일경우 
            # [5,5,5,6,6]

            for i in range(n - others) :
                answer.append(tmp)
            
            for i in range(others) :
                answer.append(tmp+1)
                
            return answer 

================================================================
#1차시도 => 테스트케이스만 통과하는구나....ㅠ
def solution(n, s):
    answer = []
    #N개의 자연수의 합이 S가 되는 집합 
    #곱이 최대여야 함..! => 중간값들을 곱하는 것이.. 최댓값..!
    
    if s % n == 0 : #나눠지는 경우
        tmp = int(s / n) 
        return [tmp] * n     
        
    else :
        tmp = s // n 
        if tmp == 0 :
            return [-1] 
        else :
            ##### 이부분이 문제였다..! #####  
            #왜 tmp+1 을하는가, 나머지개수만큼의 tmp+1 숫자를 append시키면되는데!!! 
            # N = 5, S = 27 일경우 => [5,6,7,8,9] 그럼 합이 다르게 나와요..ㅠㅠ;; 
            
            for i in range(n) :
                answer.append(tmp)
                tmp +=1 
                
            return answer 
          
