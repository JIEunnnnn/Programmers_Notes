#LV.3 줄서는방법
#주어진 N명의 사람들을 k번째로 줄세울때 나오는 리스트 
#
#대박적..두달만에 풀어보니 성공...
#재귀를 활용해야하는데 함수정의하기 헷갈려서 while 문 활용했다 :)

import math

def solution(n, k):
    answer = []
    
    people = [i for i in range(1,n+1)]
    
    while k != 1 :
        fac = math.factorial(len(people))
        check = fac//len(people) 
        idx = 0
        for i in range(n):
            if k <= (i+1)*check :
                idx = i 
                k -= (i*check)
                break 
    
        answer.append(people[idx])
        people.pop(idx)
        
        if k == 1 :
            answer.extend(people)
    
    
    return answer

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

