#순엿 => 순서고려한다 (BC, CB), 조합 => 순서고려하지않는다 (BC만)

#2차시도(조합) => 시간초과 
from itertools import combinations 

def solution(number, k):
    size = len(number) - k
    number = list(number)
    
    
    list2 = list(map(''.join, combinations(number,size) ))    
    answer = max(list2)
    
    #answer = ''
    return answer

=================================================================
#1차시도(순열)
from itertools import permutations

def solution(number, k):
    size = len(number) - k
    number = list(number)
    print(number)
    
    #list2 = list(permutations(number,size))
    list2 = list(map(''.join, permutations(number,size) ))
    #print(list(list2))
    list3 = list2.sort(reverse=True)
    answer = list3[0]
    print(answer)
    
    #answer = ''
    return answer
