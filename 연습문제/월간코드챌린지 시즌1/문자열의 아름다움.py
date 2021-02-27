#월간코드 챌린지 시즌1 문자열의 아름다움
#주어진 규칙에 따라 아름다움의 합을 구하기
#
#
#


#1차시도
#시간초과 및 정확도 
def solution(s):
    answer = -1
    
    
    #문자열모두가 동일한 경우
    for i in s :
        count = 1
        if i != s[0] :
            break
        else :
            count+=1
            
        if count == len(s) :
            return 0
    
    list_cnt = []
    
    for i in range(len(s)) :
        count = 0
        tmp = s[i]
        for j in range(i+1, len(s)) :
            if tmp != s[j] :
                count+=1
                #print("text1")
                #print(tmp)
                #print(s[j])
                #print(count)
                list_cnt.append(count)
            else :
                #print("text2")
                #print(tmp)
                #print(s[j])
                #print(count)
                list_cnt.append(count)
                count+=1
    
            
    #print(count)  
    #print(list_cnt)
    
    return sum(list_cnt)
