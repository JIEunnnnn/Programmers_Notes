#LV.1 2016
#주어진날짜에 무슨요일인지 계산하는 알고리즘
#
#딕셔너리활용 및 dic[key] 활용해서 value값 리턴
#for문에서는 items() 메소드 이용!! => 전체 key와 value값 가져오는 메소드

def find_key(dict, val):
    return next(key for key, value in dict.items() if value == val)

def solution(a, b):
    
    
    #윤년계산법
    #나누기 4 해서 0으로 떨어지면 윤년! + 100으로 나눠떨어지면 안됨!
    #2월이 29일
    month = { 1 :31, 2 : 29, 3 : 31, 4: 30, 5 : 31, 6: 30, 7 :31,
           8 : 31, 9 :30, 10 :31, 11 :30, 12: 31}
    
    day = {3:"SUN",4: "MON", 5:"TUE", 6: "WED",
           0: "THU",1: "FRI", 2: "SAT"}
    
    
    count = 0
    for key, values in month.items() :
        if key == a :
            count+=b
            #print(count)
            break 
        else :
            count += values 
            #print(count)
    
    
    tmp = count % 7
    #print(tmp)
    
    #print(day.keys())
    #print(day.values())
    
    if tmp in day.keys() :
        return day[tmp]
