
====================================================================
#1차시도

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
    
