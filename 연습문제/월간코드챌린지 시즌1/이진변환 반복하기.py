#월간코드챌린지 시즌1 이진변환 반복하기
#주어진 문자열에서 0을 제거하고, 최종 1만 남을때까지 몇번 계산했는지, 몇개의 0을 제거했는지 구하는 문제 
#
#s가 문자열이므로 조건식을 문자열로 체크해야했당..(아니면 무한루프~!)
#format()함수활용해서 2진법변환!! >_< 내장함수최고다 이말이야~~~ 

def solution(s):
    
    num = 0
    cnt = 0
    tmp_size = ''
    while s != '1' :
        num += s.count("0")
        tmp = s.replace("0","")
        tmp_size = len(tmp)
        
        #s = bin(tmp_size)
        s = format(tmp_size, 'b')
        #print(s)
        #print(type(s))
        cnt +=1 
        #print(k)
        #break
        
        
    return [cnt, num]
  
