#2019 KAKAO BLIND RECRUITMENT 오픈채팅방
#카카오톡 오픈채팅방에 대한 로그 출력, 닉네임 변경시 + 재출입시 새로운 닉네임 고려
#
#for문2번돌려서 시간초과 발생할줄 알았는데.. 다행히 정확도만 고려하는 문제였다
#다르게 푸는 방법도 고려해봐야하나?


def solution(record):
    answer = []
    inpeople = {}
    for r in record :
        abc = r.split()
        #print(abc)
        
        if abc[0] =='Enter' :
            
            answer.append( abc[1] + "님이 들어왔습니다.")
            inpeople[abc[1]] = abc[2]
            
        elif abc[0] == 'Change' :
            
            inpeople[abc[1]] = abc[2]
        
        elif abc[0] == "Leave" :
            answer.append(abc[1] +"님이 나갔습니다." )


            
            
    answerlist = []
    for a in answer :
        idx = a.find('님')
        abc = a.replace(a[:idx], inpeople[a[:idx]])
        answerlist.append(abc)
        
    return answerlist
