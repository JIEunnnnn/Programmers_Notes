#LV.3 단속카메라 
#진입-진출기준으로 최소 몇개의 카메라 필요한가? 
#
#
#https://bladejun.tistory.com/43

def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[0], reverse=True)
    #[[-5, -3], [-14, -5], [-18, -13], [-20, 15]]
    
    now = routes[0][0]
    for i in routes[1:]:
        if i[1] >= now: #진출시점이 진입카메라보다 같거나 클경우 (교차지점) 
            continue 
        else:
            now = i[0]
            answer += 1
    
    return answer

========================================================
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
