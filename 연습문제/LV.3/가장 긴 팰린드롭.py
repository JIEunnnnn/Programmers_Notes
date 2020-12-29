


==========================================================
#2차시도

def solution(s):
    answer = 0
    
    list_s = list(s)
    print(list_s)
    
    while list_s :
        for i in range(len(list_s)) :
            if list_s[i] != list_s[-i-1] :
                list_s.pop()
                break
            elif list_s[i] == list_s[-i-1] :
                answer+=1 
            
            if i == len(list_s) -1 :
                print(list_s)
                return answer
            
#1차시도
#정확성과 효율성...0점

def solution(s):
    answer = 0

    list_s = []
    for i in s :
        if len(list_s) > 1 :
            top = list_s[-1]
            cmp = list_s[-2]
            
            if i == cmp :
                answer+=2
                list_s.pop()
                
                if len(list_s) == 1 :
                    if list_s[-1] == i :
                        answer+=1
                        return answer
            else :
                list_s.append(i)
                
            
        else :
            list_s.append(i)

    print(list_s)
    #return answer
