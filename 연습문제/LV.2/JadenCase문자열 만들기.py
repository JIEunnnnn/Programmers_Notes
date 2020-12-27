#LV.2 JadenCase 문자열 만들기 
#문장의 첫단어는 대문자,나머지는 소문자로 변환시키는 알고리즘 
#
#처음에 정확성 오류난것은 " hello" > " Hello" 과 같이 공백관련을 생각하지않아서...발생한것이었다.
#또한, 문자열을 리스트로 변환해서 for문을 돌렸는데.... 파이썬은 문자열,리스트,튜플로 for문바로 돌릴수있다는 특징:) 을 잊고있었다!

def solution(s):
    answer = ''
    flag=0
    for i,v in enumerate(s) :
        if v == ' ' :
            answer+=' '
            flag=1
        elif (flag==1 and v != ' ') or i==0 :
            flag=0
            answer+=v.upper()
        else:
            answer+=v.lower()
            
        #print(v)
        
    #print(answer)
    return answer

=============================================================
#1차시도
#정확성오류...40점 

def solution(s):
    s_list = s.split()
    tmp_list = []
    for i in s_list :
        tmp =i[0].upper() + i[1:].lower()
        tmp_list.append(tmp)
        
    return ' '.join(tmp_list)
