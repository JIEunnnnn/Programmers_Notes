#LV.1 핸드폰 번호 가리기
#마지막 4자리만 번호출력하는 알고리즘
#
#문자열슬라이싱 활용! 
#리스트컴프리헨션으로 처음 answer정의하려고했는데, 문자열이라는것을 잊고있었다! 
# 리스트에서만 활용가능한기법 

def solution(phone_number):
    answer = ""
    
    
    for i in phone_number[:-4] :
    #   for i in range(0, len(phone_number[0:-4])):    
        answer += "*"
    
    answer += phone_number[-4:]
    
    return answer
    
