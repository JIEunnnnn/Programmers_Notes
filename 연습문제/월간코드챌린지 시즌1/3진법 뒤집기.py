#월간코드챌린지 시즌1 3진법 뒤집기!
#자연수 => 3진법 => 뒤집기 => 10진법 변환과정거치는 문제
#
#기존에 존재하던 int(문자열, 변환할진수) 를 사용하지못해서 당황스러웠음... 
#나머지연산과 나눗셈활용해서 문제풀었다..ㅎ...


def solution(n):
    tmp = n
    abc = []
    
    while tmp != 0 :
        i = tmp % 3
        tmp = tmp // 3 
        abc.append(i)
        #print(i)
    
    print(abc)
    abc.reverse()
    
    num = 0
    answer = 0
    for i,v in enumerate(abc) :
        #print(i)
        #print(v)
        answer += 3**i*v
        #answer = 
    
    
    return answer
