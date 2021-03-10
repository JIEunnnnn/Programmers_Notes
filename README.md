## Programming_Notes
> 1일1코테중 
>> 프로그래머스 문제풀이  
https://programmers.co.kr/learn/challenges  
   
  
<br>    

## 파이썬 기본문법
>  파이썬자료형
>>  int(숫자)  
    dict(매핑/ 키와자료형으로 구성된 복합자료형) -> 키값 중복X
    set(집합/ 중복된 값을 갖지않는다) -> 중복된값들 처리할때 활용  
    list(리스트/ 동적배열)  
    str,tuple,bytes(시퀀스/ 불변 및 순서가있는 수열)

> DFS&BFS 
>> DFS는 스택, BFS는 큐로 구현한다..!    
>> 
> 진수변환  
>> 10 -> 2진수 : bin(x) / format(x, 'b') <-> int(y, 2)  
   10 -> 8진수 : oct(x) / format(x, 'o')  <-> int(y, 8)
   10 -> 16진수 : hex(x) / format(x, 'h') <-> int(y, 16)

<br>


## 파이썬 기본라이브러리


>    1. 기본 메소드  
     sorted #리스트데이터를 오름차,내림차순 정렬 (b=sorted(a,조건), a.sort(조건)) 
     push, pop #popleft (deque라이브러리사용)  
     append
     map #리스트형식의 변수타입변환 OR lambda 적용시 사용, , list의 element에 함수를 적용시켜 결과를 반환하고 싶을 때 사용  
     filter #리스트를 lambda를 활용하여 조건에 맞게 추출할수있는 메소드  
     reduce #리스트의 원소를 누적시(ex,총합) 활용
     
>    2. collections 라이브러리  
     counter #단어->알파벳갯수와 최다출현을 딕셔너리로 반환 ex) {'headgear': 2, 'eyewear': 1}  
     defaultdict #dict형태를 데이터를 append(리스트메소드)사용하고 싶을 때 
     
>    3. operator 라이브러리  
     itemgetter #다차원리스트 정렬시킬때 활용하는 라이브러리   
     
>    4. itertools 라이브러리  
     permutations #순열과 조합 관련 문제풀때 용이  #중복을 허용하지않는 순열  
                  
>    5. math 라이브러리    
     sqrt #제곱근 연산시...(소수판별할때 제곱근으로 판별해야함 => 시간초과)  ex) math.sqrt(x)  
     round, ceil, floor, trunc #반올림, 올림, 내림, 버림                    ex) math.ceil(x)  
     gcd #최대공약수 ex) math.gcd(n,m)  
     
>    6. heaqp 라이브러리    
    이진트리 기반의 최소 힙 자료구조 => 리스트를 매번 정렬해야하는 효율성을 감소시킬수있다. 
    
>    7. numpy 라이브러리    
    행렬문제 풀때 유용한듯... 공부해야할라이브러리!! 
    
