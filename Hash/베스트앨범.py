#람다는 다른함수의 인수를 넣을때 사용하는 표현식!!! 
#defaultdict 은 dict형태를 데이터를 append(리스트메소드)하고싶을때사용하는 라이브러리

from collections import defaultdict

def solution(genres, plays):
    answer = []
    genr_dict = {} 
    #{장르 : 총합계}
    genr_index_dict = defaultdict(lambda: []) #람다를 활용한 초기값 표현
    #[장르 : (인덱스, 횟수)]
     
    
    for i in range(len(plays)):
        g = genres[i]
        p = plays[i]
        
        if g not in genr_dict :
            genr_dict[g] = p 
            #genr_index_dict[g]=i,p
            genr_index_dict[g].append((i,p))
        else :
            genr_dict[g] += p
            #genr_index_dict[g]=i,p
            genr_index_dict[g].append((i,p))
            
    print(genr_dict)  
    print(genr_index_dict)
    #print(genr_index_dict.keys())
        
    genr_dict = sorted(genr_dict.items(), reverse=True, key=lambda item: item[1])
    #lamda함수 활용하여 dict 정렬하기
    
    print(genr_dict) 
    
    for j in range(len(genr_dict)): #list
        for i,d in genr_index_dict.items() : #dict
            d.sort(key=lambda x : x[1], reverse=True) 
            # (인덱스, 재생횟수) 에서 횟수기준으로 내림차순
            if genr_dict[j][0] in i :
                
                
                if len(d) > 1 :
                    print(d)
                    answer.append(d[0][0])
                    answer.append(d[1][0])
                else :
                    answer.append(d[0][0])
                
                
                
            
            
    return answer
