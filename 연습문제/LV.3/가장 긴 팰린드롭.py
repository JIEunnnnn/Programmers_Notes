
==========================================================
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
