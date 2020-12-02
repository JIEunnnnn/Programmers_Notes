
#2차시도
def solution(scoville, K):
    answer = 0
    #filter_scov = list(filter(lambda x : x < K, scoville))
    scoville.sort()
    while min(scoville) < K :
        answer += 1 
        tmp = scoville.pop(0)     
        tmp2 = scoville.pop(0)
        scoville.append(tmp + tmp2 *2)
        scoville.sort()
        
        if len(scoville) == 1 :
            answer = -1
            break

    

    return answer
    
#1차시도
def solution(scoville, K):
    answer = 0

    filter_scov = list(filter(lambda x : x < K, scoville))

    for i in filter_scov :
        print(i)
        if i < K :
            tmp = i + (i+1)* 2 
            filter_scov.pop(0)
            filter_scov.pop(0)
            filter_scov.append(tmp)
            filter_scov.sort()
            answer +=1
        else :
            break 
        
    if filter_scov[0] < K :
        answer = -1
    #print(filter_scov)

    

    return answer
