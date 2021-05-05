#Summer,Winter Coding(~2018) 방문길이
#명령어에 따른, 이동거리 구하기 
#
#최초로가는 길만 세기 + 지도밖으로 나가지않기! 
#백준으로 훈련해서 쉽게 풀수있었던 문제!

def solution(dirs):
    
    goto = {'U' : (0,1), 'D' : (0,-1), 'R' : (1,0), 'L' : (-1,0)}
    
    x, y = 0, 0 
    cnt = 0
    stack = []
    
    for d in dirs :
        tx, ty = goto[d]
        dx, dy = tx + x, ty + y 
        if -5 <= dx <= 5 and  -5 <= dy <= 5 :
            if (x,y,dx,dy) not in stack and (dx,dy,x,y) not in stack :
                cnt +=1 
                stack.append((x,y,dx,dy))
            
            x,y = dx, dy
    
    
    return cnt 
====================================================================

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
  
