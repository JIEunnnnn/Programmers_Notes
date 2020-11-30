#LV.2 전화번호 목록
#접두사로 시작되는 번호 존재할경우 False 반환 
# 
#조건문 in 대신 startswith() 메소드사용 


def solution(phone_book):
    answer = True
    
    print(len(phone_book))
    while len(phone_book) :
        phone_book.sort() #정렬이유 => 1234, 123 로 존재할경우 123 이 접두사임에도 발견못하기때문 :) 
                          #원본정렬
                          #sorted() : 원본냅두고 새로 정렬 => phone_book2 필요
                      
        compare_Case = phone_book.pop(0)
        
        #phone = [phone for phone in phone_book if compare_Case in phone]
        phone = [phone for phone in phone_book if phone.startswith(compare_Case)]
        
        if phone != [] :
            answer = False
            break


    return answer
