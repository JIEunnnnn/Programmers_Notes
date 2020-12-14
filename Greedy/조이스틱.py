

===============================================================
#1차시도 
#정확성 54 .... 

def solution(name):
    
    answer = 0

    front = ord('A')
    end = ord('Z')
    
    tmp = 0
    for i in name :
        
        if i == 'A' :
            print(i)
            tmp +=1 
        else :
            if abs(ord(i) - front) > abs(ord(i) - end) :
                print(i)
                print(ord(i))
                answer +=1
                answer += abs(ord(i) - end )
            elif abs(ord(i) - front) < abs(ord(i) - end ) :
                print(i)
                answer += abs(ord(i) - front)
            else :
                print(i)
                answer += abs(ord(i) - front)
    

    answer += len(name)
    answer -= 1 
    answer -= tmp
    
    return answer
