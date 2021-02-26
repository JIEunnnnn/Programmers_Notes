#월간코드챌린지 시즌1 3진법 뒤집기!
#자연수 => 3진법 => 뒤집기 => 10진법 변환과정거치는 문제
#
#기존에 존재하던 int(문자열, 변환할진수) 를 사용하지못해서 당황스러웠음... 
#나머지연산과 나눗셈활용해서 문제풀었다..ㅎ...
#아니네.. int는 2,3,4 -> 10진법 변환시키는 함수니까 오류가나지...ㅎㅎ;;

#다른사람풀이
def solution(n):

    three = ''

    # 3진법 변환
    while n>2 :
        n,m = divmod(n,3) 
        #몫과 나머지!! 
        
        three += str(m)

    three += str(n) 
    #마지막몫이 0,1,2 중 하나이므로 three 에 더해서 10진법으로 변환..!

    # 10진법으로 변환
    return int(three,3)

=====================================================================

def solution(n):
    tmp = n
    abc = ''
    
    while tmp != 0 :
        i = tmp % 3
        tmp = tmp // 3 
        abc+=str(i)
    
    print(abc)
    
    num = 0

    
    
    return int(abc,3)


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
