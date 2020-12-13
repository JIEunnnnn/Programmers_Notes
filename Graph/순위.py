
==========================================================
#1차시도
#정확성...20점ㅠㅠ

def solution(n, results):
    answer = 0
    #횟수로 따지면 되는거같기도하고 ㅇㅅ< 
    print(results)
    win_results = {}
    lose_results = {}
    answer_people = []
    
    for i in results :
        if i[0] not in win_results :
            win_results[i[0]] = 1 
        else :
            tmp = win_results[i[0]]+1
            win_results[i[0]] = tmp
            
        if i[1] not in lose_results :
            lose_results[i[1]] = 1
        else :
            tmp = lose_results[i[1]] +1
            lose_results[i[1]] = tmp
    
    print(win_results)
    print(lose_results)
    
    i=0
    while  i< n :
        print(i)
        if i in win_results :
            win_tmp = win_results[i]
        else :
            win_tmp = 0
        if i in lose_results :
            lose_tmp = lose_results[i]
        else :
            lose_tmp = 0
            
        if lose_tmp + win_tmp == n-1 :
            print("테스트중")
            answer +=1 
            answer_people.append(i)
            print(i)
            
        i+=1 
        
    #2번
    for i in answer_people :
        print(i)
        tmp = 0
        tmp2 = 0
        for j in results :
            if i == j[0] :
                tmp += 1
                #print("테스트2")
                #print(i)  
                #print(j)
            if i == j[1] :
                tmp2 +=1 
        if tmp == 1 :
            answer += 1
        if tmp2 == 1 :
            answer += 1 
                
    
        #if i[1] in answer_people :
            
    
    
    return answer
