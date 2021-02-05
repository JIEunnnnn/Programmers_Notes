#2017팁스타운 짝지어제거하기 
#2번 중복되는 문자열을 제거하는 규칙을 통해 0이 되는가? 
#
#스택구조활용하여 문자열 제거 
#

def solution(s):
    answer = 0
    stack = []

    for i in s :
        
        if len(stack) == 0 :
            stack.append(i)
            continue 
        
        if stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
            
    #print(stack)       
    return answer if len(stack) != 0 else 1
