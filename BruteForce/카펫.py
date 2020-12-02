#LV.2 카펫
#주어진 brown.yellow 갯수에 따른 직사각형크기 구하기
#
#넓이를 통해 약수리스트를 추출하고, 주어진패턴을 활용하여 1. (가로-2)(세로-2) = 노랭이, 2. 가로*세로 - 노랭이 = 브라운 식으로 구했다. 
#가장참신했던 답은 둘레길이를 통해 구하는 것..! 
#효율성체크는 없어서 다행이지만ㅠ O(n) 두번나오는것같아서 아쉽ㅠㅠ 

def solution(brown, yellow):
    area = brown+yellow
    num_list = []
    answer = []
    
    for i in range(1, area+1) :
        if area%i == 0 :
            num_list.append(i)
    
    for i in num_list : #가로
        j = int(area/i) #세로
        
        if (i-2) * (j-2) == yellow :
            #print("안지나침?")
            if i * j - yellow == brown :
                if i < j : #sort()로 해결가능하겠네ㄷ 
                    answer.append(j)    
                    answer.append(i)
                else :
                    answer.append(i)    
                    answer.append(j)
                break    
    
    return answer
