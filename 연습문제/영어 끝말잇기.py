#Summer/Winter Coding(~2018) 영어 끝말잇기
#1. 끝단어가 다를경우 2. 단어 2번말하는 경우 경기종료
#
#경우의 수 따지는게 조금 복잡한 것 외에는 어렵지않았다. 
#

def solution(n, words):
    
    people = [ '' for i in range(n) ] 
    stack_dic = []
    
    num = 0 #몇번째 사람
    count = 1 #경기회전수, 처음시작은 첫번째..!  
    last = ''
    for i in words :
        
        if last : #마지막단어가 존재하면

            # 말했던 문자 말하는 경우
            if stack_dic :
                if i in stack_dic : 
                    return[num+1,count]

            # 끝자리에 대한 단어가 아닌경우 
            if last[-1:] != i[:1] :
                return[num+1,count]
        
        people[num] = i 
        stack_dic.append(i)
        last = i 
        if num == n -1 : #오버플로우 방지
            num = 0
            count +=1 
        else :
            num +=1 
            


    return [0,0]
