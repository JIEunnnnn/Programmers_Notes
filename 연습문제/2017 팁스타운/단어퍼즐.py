#2017팁스타운 단어퍼즐
#주어진 단어조각을 이용하여 문장완성하는 퍼즐
#
#DP를 활용해야했으며..문자열슬라이싱 특징과 문제조건 다시살펴보자...  
#https://dev-note-97.tistory.com/177

import math

def solution(strs, t):
    answer = 0
    default = math.inf #양의 무한대
    
    dp = [default for i in range(len(t)+1)]
    dp[0] = 0
    for i in range(1, len(t)+1) :
        j = i - 5 if i > 5 else 0 
                            #조각의 길이는 5이하이므로 
        
        while j < i:
            if dp[j]+1 < dp[i] and t[j:i] in strs : 
                                        # j <= a < i
                dp[i] = dp[j]+1
            j+=1
            print(dp)
    
    print(default) #inf 
    print(dp[len(t)]) #최솟값.. 
    
    return  dp[len(t)] if dp[len(t)] != default else -1

====================================================================
#2차시도 => 이렇게 하는게 맞는지 막막하다.... 

def solution(strs, t):
    answer = 0
    
    print(list(t))
    t_list = list(t)
    tmp = ''
    stack = []
    
    
    while t_list :
        tmp += t_list[0]
        print(tmp)
        
        if tmp in strs :
            print("테스트")
            stack.append(tmp)
            
            print(tmp)
        
        t_list.pop(0)


    

    return answer


#1차시도 => 중복허용 조합을 일으키면... 안되지..효율성극악..
from itertools import combinations_with_replacement
	["ab", "na", "n", "a", "bn"], "nabnabn"
def solution(strs, t):
    answer = 0
    
    for sz in range(len(strs)) :
        print(sz)
        cmp = list(combinations_with_replacement(strs, sz))
        for i in cmp :
            print(''.join(i))
            if t == ''.join(i) :
                print(t)
                return sz
        
        
    

    return answer
    
