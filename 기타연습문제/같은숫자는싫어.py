#LV.1 같은숫자는싫어! 
#리스트내에 중복된숫자 제거하는 문제 
#
#stack구조 이용 
3#

def solution(arr):
    
    answer = [arr[0],]
    top = answer[-1]
    for i in arr :
        if i != top :
            answer.append(i)
        top = answer[-1]
    
    
    return answer
