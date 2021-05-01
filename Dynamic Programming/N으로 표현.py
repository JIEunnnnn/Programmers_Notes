#LV.3 N으로 표현
#N이라는 숫자를 number로 표현하는데, 몇개 필요한가?
#
#어떻게 조합을 해야할지 헤멤... :( 
#https://www.hamadevelop.me/algorithm-n-expression/

from itertools import combinations


def will_list(N, i) :
    list_num = []
    tmp = [N for i in range(i)]
    print(tmp)    
    
    for r in range(i,-1,-1) :
        print(tmp[:r])
        print(tmp[r:])
    

def solution(N, number):
    possible_set = [0,[N]] 
    if N == number: 
        return 1
    for i in range(2, 9): 
        case_set = [] 
        basic_num = int(str(N)*i)  #연속으로 붙는 값
        case_set.append(basic_num)
        for j in range(1, i//2+1): 
            #절반이후에는 동일한 값 반복 
            # ex) [555, 0] [55, 5] [5, 55] [0, 555]
            #print(possible_set[i-j]
            for x in possible_set[j]:
                for y in possible_set[i-j]: #i=2일때 possible_set 의 len = 2, j=1
                                            #        x = possible[1], y=possible[2-1] ==> append
                    
                                            #i=3일때 possible_set 의 len = 3 , j=1
                                            #        x = possible[1] y= possible[3-1] ==> append
                        
                                            #i=4일때 possible_set 의 len = 4 , j=1,2
                                            #        x = possible[1] y= possible[4-1] ==> append
                                            #        x = possible[2] y= possible[4-2] ==> append
                              
                    case_set.append(x+y)
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y !=0:
                        case_set.append(x/y)
                    if x !=0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set) 
            
    return -1
  
