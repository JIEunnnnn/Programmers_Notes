from operator import itemgetter

def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    i=0
    j=0
    k=0 
    count_a1= 0 
    count_a2 = 0
    count_a3 =0
    for ans in answers : #정답배열
        
        if ans == a1[i]:
            count_a1 +=1
        if ans == a2[j] :
            count_a2 +=1 
        if ans == a3[k]:
            count_a3 +=1
            
        #초기화하는방법    
        if i == 4:
            i = 0
        else :
            i += 1  
            
        if j == 7:
            j = 0
        else :
            j += 1 
        
        if k == 9:
            k = 0
        else:
            k += 1
            
    #max = [count_a1, count_a2, count_a3]
    max = [
        {'key' : 1 ,'count': count_a1},
        {'key' : 2, 'count' : count_a2},
        {'key': 3, 'count': count_a3 }    
    ] 
    listmax = sorted(max, key=itemgetter('count'), reverse=True ) 
    
    sz = 0 
    compare = listmax[sz]['count']
    while sz < len(listmax) :
        if compare == listmax[sz]['count'] :
            answer.append(listmax[sz]['key'])     
        
        sz +=1
        
    return answer
