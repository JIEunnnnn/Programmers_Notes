


=====================================================
#1차시도 
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
