#LV.1 서울에서 김서방찾기
#주어진 리스트에서 kim에 해당되는 위치반환
#
#enumerate() 함수와 int변환하는 str()함수 이용
#

def solution(seoul):
    
    for key, value in enumerate(seoul) :
        if value == "Kim" :
            return '김서방은 ' + str(key) + '에 있다'
    
