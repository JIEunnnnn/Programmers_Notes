#LV.2 올바른괄호
#주어진문자열이 ()의 올바른형식인지 따지는 알고리즘문제
#
#스택을 활용하여 비교 
#

def solution(s):
    
    if len(s)%2 != 0 :
        return False
    
    stack = []
    for i in s :
        if len(stack) == 0 :
            stack.append(i)
            continue 
            
        top = stack[-1]
        if top != i :
            if top == "(" and i == ")" : => ())()) 과같은 경우를 대바한 조건문
                stack.pop()
            else :
                return False
            
        else :
            stack.append(i)
        
    if len(stack) == 0 : #s[-1]==")"
        return True
    else :
        return False
