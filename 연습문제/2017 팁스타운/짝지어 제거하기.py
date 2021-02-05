#2017 팁스타운
#2번 중복되는 문자열을 제거하는 규칙을 통해 0이 되는가? 

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
