#LV.3 단어변환 
#주어진단어를 통해 한글자씩 바꾸면서 target과 일치시키기
#
#
# 방문한것을 알기위한 방문노드 필요..

def solution(begin, target, words):
    answer = 0 #DFS
    stacks = [begin]
    visited = {i:0 for i in words} 
    #{'hot': 0, 'dot': 0, 'dog': 0, 'lot': 0, 'log': 0, 'cog': 0}
    #이미 검사했던 단어를 다시 검사하지 않도록 하기 위한 딕셔너리
    if target not in words:
        return 0 #변환할수없는경우 0 반환
    
    while stacks: #스택이 존재하는동안 
        stack = stacks.pop()
        if stack == target:
            return answer
        
        for word in words:
            for i in range(len(word)):
                copy = list(word)   #비교해야할 문자열
                copy_front = list(stack) 
                                    #문자열을 리스트로 변환
                copy[i] = 0
                copy_front[i] = 0
                #한자리씩만 변경하기 위해서 0으로 처리하고 비교함..ㄷㄷ
                
                if copy == copy_front:
                    if visited[word] != 0: 
                        #visited가 1이라면 이미 검사했던 단어므로 그냥 넘어간다.
                        continue
                    visited[word] = 1 
                        #visited가 0이면 해당 단어의 visited 값을 1로 바꾼다.
                    stacks.append(word)
                    print(stacks)
                    
                    break
        answer += 1 #Depth 1추가

    return answer

====================================================
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
