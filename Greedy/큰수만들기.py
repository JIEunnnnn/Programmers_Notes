#LV.2 큰수만들기
#주어진숫자를 -K만큼의 자리수에서 가장 큰수를 출력하기 
#
#조합생각했는데 시간초과발생..
#순열 => 순서고려한다 (BC, CB), 조합 => 순서고려하지않는다 (BC만)

#https://kdgt-programmer.tistory.com/5?category=1121942

def solution(number, k):
    
    num = list(number)
    stack = [num[0]]
    count = 0
    
    for i in range(1, len(num)):
        if count == k :
            stack = stack + num[i:]
            break 
        
        stack.append(num[i])
        if stack[-1] > stack[-2] :
            while(len(stack) != 1 and stack[-1] >stack[-2] and count < k):
                stack[-2], stack[-1] = stack[-1], stack[-2]
                stack.pop()
                count +=1 
            
    return "".join(stack[:len(num)-k])

================================================================
#2차시도(조합) => 시간초과 
from itertools import combinations 

def solution(number, k):
    size = len(number) - k
    number = list(number)
    
    
    list2 = list(map(''.join, combinations(number,size) ))    
    answer = max(list2)
    
    #answer = ''
    return answer


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
