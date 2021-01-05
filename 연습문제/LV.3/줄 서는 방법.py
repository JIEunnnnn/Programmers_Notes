
=================================================================
#1차시도
#효율성 및 정확성ㅠ

from itertools import permutations

def solution(n, k):
    answer = []
    for i in range(n) :
        answer.append(str(i+1))
    
    sz = len(answer)
    list_answer = list(map(''.join, permutations(answer,sz)))
    #print(answer)
    #print(list_answer)
    result = []
    for i in list_answer[k-1] :
        result.append(int(i))
    
    #print(result)
    return result
