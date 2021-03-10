#Summer,Winter Coding(~2018) 방문길이
#
#
#
#

#1차시도 => 뭐가문제지..? 
def solution(dirs):
    answer = 0
    #0에서부터 시작
    start = [0,0]
    dir_key = { "U" : [0, 1], "D" : [0, -1], "R" : [1, 0], "L" :[-1, 0] }
    #print(dir_key)
    list_dirs = list(dirs)
    #print(list_dirs)
    
    stack = []
    
    
    for i in list_dirs :
        start[0] += dir_key[i][0] #X
        start[1] += dir_key[i][1] #Y
        print(start)
        
        if start not in stack :
            answer +=1 
        
        stack.append([start[0],start[1]])
    
    return answer
  
