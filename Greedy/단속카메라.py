

#1차시도=> 실패
from collections import deque

def solution(routes):
    
    answer = 0
    routes.sort(key = lambda x : x[1])
    print(routes)
    
    
    camera = deque() 
    for x,y in routes :
        
        if len(camera) == 0 :
            
            tmp = list(i for i in range(x,y+1))
            camera.append(tmp)
        else :
            for t in range(x,y+1) :
                abc = []
                if t in camera :
                    abc.append(t)
            
            if len(abc) != 0 :
                camara = abc 
            else :
                answer +=1 
                camera = deque()
        

    return answer
