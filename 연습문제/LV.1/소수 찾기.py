#LV.1 소수찾기
#1부터 N까지 중에서 소수 몇개인지를 찾는 문제
#
#전체 for문돌리면 시간초과 발생.. => 제곱근 개념 활용해서 효율성문제 해결
#https://wikidocs.net/21638  (소수판별참고페이지)


import math

def is_prime_number(x) :
    array = [1 for i in range(x)]
    array[0] = 0 #1은 소수가 아니므로 0 으로 설정 
    
    #print(array)
    m = int(math.sqrt(x)) #제곱근까지 검사
     
    for i in range(2, m+1):
        
        if array[i-1] == 1 : #소수일경우 
            for j in range(i+i, x+1, i) : # 소수의 배수들은 배수로 설정! (ex, 2일경우 4, 6, 8 , 10 )
                                          # 주어진 숫자 X까지 i 배수 검사!!
                
                    array[j-1] = 0
                    
    #print(array)
    return sum(array)
    

def solution(n):
    
    answer = is_prime_number(n)
    return answer


======================================================================
#1차시도 => 시간초과..

import math

def is_prime_number(x) :
    array = [1 for i in range(x)]
    array[0] = 0 
    #print(array)
    
    # int(math.sqrt(x))+1) 경우는 주어진 X가 소수인지 판별하기위한...! 
    for i in range(2, x+1):
        if array[i-1] == 1 : 
            for j in range(2, i+1) :
                if i % j == 0 and i != j:
                    array[i-1] = 0
                    #print("테스트")
                    #print(i)
                    #print(j)
                    continue 
                    
    #print(array)
    return sum(array)
    

def solution(n):
    
    answer = is_prime_number(n)
    
    return answer
  
