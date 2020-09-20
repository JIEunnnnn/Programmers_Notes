# LV.1 완주하지못한선수


def solution(participant, completion):
    
    participant = sorted(participant, reverse=True) #리스트를 오름차순으로 정렬시키기
    completion = sorted(completion, reverse=True)
    answer = '' 

    
    while len(completion) : #완수자 리스트 크기만큼 반복문실행 
        compare_com = completion.pop() 
        compare_part = participant.pop()
        
        if compare_part != compare_com :
            answer = compare_part
            break 
        
    if answer == '' :  #완주자만큼 반복문 실행해도 답이없다? 그럼 참여자리스트에 미완수자존재 :)
        answer = participant.pop()
        

    return answer
