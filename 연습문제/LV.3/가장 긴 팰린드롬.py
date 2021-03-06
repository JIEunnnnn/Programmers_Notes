#LV.3 가장 긴 팰린드롬
#문자열에서 가장 긴 회문을 찾기
#
#스택, 리스트 시도해보고 슬라이싱 이용하여 회문판별하는 것으로 구현
#3차시도시. 회문판별구현 코드가 시간초과발생.. 4차시도에서 슬라이싱역순을 활용하여 재구현! 
#회문은 역순으로 동일해야한다는것을 까먹지말자:)

def palidrome(word) : #회문판별식 
    return word == word[::-1]

def solution(s):
    answer = 0
    pali_list = [1,]
    
    for i in range(len(s)) :
        for j in range(i+1,len(s)) :
            tmp = palidrome(s[i:j+1])
            if tmp == True :
                pali_list.append(len(s[i:j+1]))
    
    return max(pali_list)

==========================================================
#3차시도 => 효율성..

def palidrome(word) : #회문판별식 
    is_palindrome = True                 
    for i in range(len(word) // 2):      
        if word[i] != word[-1 - i]:     
            is_palindrome = False        
            break
    return is_palindrome

def solution(s):
    answer = 0
    pali_list = [1,]
    
    for i in range(len(s)) :
        for j in range(1,len(s)) :
            tmp = palidrome(s[i:j+1])
            if tmp == True :
                pali_list.append(len(s[i:j+1]))
    
    return max(pali_list)

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
