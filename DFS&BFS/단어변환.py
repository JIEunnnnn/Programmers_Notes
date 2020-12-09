#2차시도 

#테스트케이스는 맞췄으나 정확성오류
def solution(begin, target, words):
    if target not in words :
        print("없음")
        return 0 
    
    list_begin = begin[:]
    list_target = target[:]
    err = 0
    for i,v in enumerate(list_target) :
        
        if list_begin[i] != list_target[i] :
            err += 1
            
    dict_list = {}
    
    for i in words :
        tmp = i[:]
        count = 0
        for j,v in enumerate(list_target) :
            if tmp[j] == list_target[j] :
                count +=1 
        dict_list[count] = dict_list.get(count,'' ) + i + ","
        #routes[i[0]] = routes.get(i[0], []) + [i[1]]
    
    print(len(dict_list))
    print(dict_list)
    
    answer = len(dict_list) +1 
    if err == 1 :
        answer = 1
    return answer
====================================================
#1차시도

#https://rfriend.tistory.com/327 문자열관련메소드

def solution(begin, target, words):
    #chr ord
    list_begin = begin[:]
    list_target = target[:]
    ord_begin = 0
    ord_target = 0
    
    for i in list_begin :
        for j in list_target :
            ord_begin += ord(i)
            ord_target += ord(j)
    
    dict_words = {}
    
    for i in words : 
        
        
    
    print(ord_begin)
    print(ord_target)
    
    
        
        
    answer = 0
    return answer
