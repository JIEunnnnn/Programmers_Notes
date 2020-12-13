#LV.3 순위
#주어진 자료를 보고 정확하게 순위를 매길수있는 사람구하기
#
#시도는 거의 유사했으나 문제를 제대로 이해못함 
#defaultdict 을 통해 초기화가능!! 


#i를 이긴 사람들에게 이긴 사람들은 전부 i를 이길 수 있다
#i에게 진사람들은 i가 진사람들에게도 전부 진다.

from collections import defaultdict

def solution(n, results):
    answer = 0
    
    #defaultdict은 기본값을 숫자,리스트,셋등으로 초기화가능
    win = defaultdict(set)
    lose = defaultdict(set)
    
    
    for a,b in results :
        win[a].add(b)
        lose[b].add(a)
    
    #print(win)
    #print(lose)
    
    for i in range(1, n+1) :
        for loser in win[i] :
            lose[loser] |=lose[i] # |= update의미함
            # 4에게 진 숫자 3,2 
            # 숫자 3,2 역시 4가 진것에서는 지는 경기임 => update
            
        for winner in lose[i] :
            win[winner] |= win[i]
            #3을 이긴 4
            #숫자 4는 3이 이긴 모든숫자(2) 를 이긴다 
    
    #print(win)
    #print(lose)
           
    for i in range(1, n+1) :
        if len(win[i]) + len(lose[i]) == n-1 :
            answer+=1 
            
    return answer

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
