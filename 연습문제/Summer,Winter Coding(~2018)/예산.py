#Summer,Winter Coding(~2018) 예산
#
#
#
#

#런타임에러 
from itertools import combinations_with_replacement
#중복조합 combinations_with_replacement(반복 가능한 객체, r)
#중복순열 product(반복 가능한 객체, repeat=1)

def solution(d, budget):
    
    d.sort() 
    cnt = 0 
    while True :
        tmp = 0
        for i in d : 
            tmp += i
            cnt += 1 
            if tmp == budget :
                return cnt 
            if tmp > budget :
                break 
        d.pop(0)
        cnt = 0
    
    return cnt
