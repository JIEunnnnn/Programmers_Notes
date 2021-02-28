#LV.1 소수찾기
#1부터 N까지 중에서 소수 몇개인지를 찾는 문제
#
#
#


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
  
