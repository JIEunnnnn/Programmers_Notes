def solution(sizes):
    answer = 0
    
    siz = []
    for i in sizes :
        if i[0] >= i[1] :
            siz.append([i[1], i[0]])
        else :
            siz.append([i[0], i[1]])
    #print(siz)
    #print(max(siz, key = lambda x : x[0]))
    #print(max(siz, key = lambda x : x[1]))
    
    sx = max(siz, key = lambda x : x[0])
    sy = max(siz, key = lambda x : x[1])
    
    answer = sx[0] * sy[1]
    return answer
