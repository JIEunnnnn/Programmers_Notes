#LV.3 이중우선순위큐
#주어진명령어에 따라 값을 삽입,삭제하는 작업수행 
#
#일반적인 리스트문제 풀때처럼 수행했는데 다른사람들은 heapq모듈의 heappush, heappop을 수행하여 정렬 안한듯 (효율성은 똥망이다..)
#이번문제는 3단계치고는 쉬운편이었던것같다... 2단계정도? 

def solution(operations):
    
    print(operations[0]) 
    answer_list = []
    for i in operations :
        abc = i.split(" ")
        if abc[0] == 'I' :
            answer_list.append(int(abc[1]))
            answer_list.sort()
        elif abc[0] == 'D' and int(abc[1]) > 0 :
            if len(answer_list) != 0 :
                answer_list.pop()
                print("#1")
                print(answer_list)
                
        else :
             if len(answer_list) != 0 :
                answer_list.pop(0)
                print("#2")
                print(answer_list)
                
    
    print(answer_list)
    if len(answer_list) != 0 :
        max_value = answer_list.pop()
        min_value = answer_list.pop(0)
        return [max_value, min_value]
    else :
        return [0,0]
