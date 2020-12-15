#LV.1 같은숫자는싫어! 
#
#
#
#

def solution(arr):
    
    answer = [arr[0],]
    top = answer[-1]
    for i in arr :
        if i != top :
            answer.append(i)
        top = answer[-1]
    
    
    return answer
