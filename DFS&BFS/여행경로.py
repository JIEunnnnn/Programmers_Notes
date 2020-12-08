#LV.3 여행경로
#주어진리스트에 따라 경로그리기
#
# 1. 딕셔너리에 여러개값을 병합하는 방법...알게됨
# 2. 리스트를 스택으로 구현하는 방법 top = stack[-1]

#리트코드 332 풀어보기

def solution(tickets):
    routes = {} #시작경로-도착경로
    
    for i in tickets :
        routes[i[0]] = routes.get(i[0], []) + [i[1]]
        #get(key, default) 키값이 존재하지않으면 default값을 가져온다.
        #딕셔너리 1개키값에 여러 값 추가하는방법... 시발        
    print(routes) 
    #	{'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}   
    
    for r in routes :
        routes[r].sort(reverse=True)
        
    stack = ["ICN",] 
    path = []
    
    while len(stack) > 0 :
        top = stack[-1] #리스트를 스택으로 구현하는 방법
        if top not in routes or len(routes[top]) == 0 :
        #routes에 키가 존재하지않거나, 키는존재하나 값이없을경우
            path.append(stack.pop())
        else :
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
        
    return path[::-1] #정렬


=====================================================
#1차시도 
#조건여러개고려해야하는게 문제.. + 시간복잡도
def solution(tickets):
    ticket_queue = []
    for i in tickets :
        if not i[0] in  ticket_queue :
            ticket_queue.append(i[0])
            if not i[1] in ticket_queue :
                ticket_queue.append(i[1])
        elif  ticket_queue.count(i[0]) > 1 :
            #둘다 동시에 있을경우...
            
        else :
            index = ticket_queue.index(i[0])
            count = ticket_queue.count(i[0])
            if len(ticket_queue) > index+1 :
                print(ticket_queue[index+1])
                print(i[1]) 
                if i[1] > ticket_queue[index+1] :
                    ticket_queue.insert(index+2, i[1])
                else :
                    ticket_queue.insert(index+1, i[1])
            else :
                ticket_queue.append(i[1])
                print(ticket_queue)
                #아예빈자리일경우 바로 append()
            
    print(ticket_queue)
    
    answer = []
    return answer
