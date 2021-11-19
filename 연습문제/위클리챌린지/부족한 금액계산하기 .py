def solution(price, money, count):
    answer = -1
    allmoney = 0
    
    for i in range(1,count+1):
        tmp = price * i
        allmoney += tmp
        
        
    #print(allmoney)
    if allmoney <= money :
        return 0
    else :
        return allmoney - money
    

    return answer
