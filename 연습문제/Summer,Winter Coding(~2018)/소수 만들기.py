#Summer/Winter Coding(~2018) 소수만들기
#주어진 리스트에서 3개의 숫자를 더한 값들 중 소수는 몇개인가? 
#
#math 라이브러리와 itertools 의 combinations(조합) 이용 
#

from itertools import combinations 
import math

def math_num(n) : #소수구할때 제곱근이용 :) 
    x = int(math.sqrt(n))
    for i in range(2, x+1) :
        if n % i == 0 :
            return False 
        
    return True 
            


def solution(nums):
    cnt = 0
    
    tmp = []
    tmp = list(combinations(nums, 3))
    #print(tmp)
    
    for i in tmp :
        num = i[0]+i[1]+i[2]
        
        if math_num(num) == True : 
            cnt +=1 
        
    return cnt
