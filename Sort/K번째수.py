#LV.1 K번째수
#주어진 array에서 지정한 인덱스값 출력
#
#list의 slice활용하여 범위자르고 sort 후 숫자찾기 :)

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)) :
        slice = array[commands[i][0]-1:commands[i][1]] 
        #start : 0부터시작이므로 -1
        #end : 지정위치-1 숫자까지 출력
        
        print(slice)
        slice.sort()
        print(slice)
        
        answer.append(slice[commands[i][2]-1])
        
    
    
    return answer
