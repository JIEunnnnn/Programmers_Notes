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
