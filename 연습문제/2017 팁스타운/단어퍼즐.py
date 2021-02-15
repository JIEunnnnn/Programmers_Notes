

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
    
