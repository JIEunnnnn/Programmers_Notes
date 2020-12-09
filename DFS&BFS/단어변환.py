
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
