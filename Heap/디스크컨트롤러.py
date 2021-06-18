#LV.3 디스크컨트롤러
#소요시간을 최소화하여 반환하기 
#
#힙구조로만 생각했는데, 2중포문돌려서 start를 더함으로써 구하는 방식도 있다는걸알게됨...ㄷㄷ 
#heapq 와 deque를 활용한 문풀....;;;

from collections import deque 
import heapq 

def solution(jobs):
    answer = 0
    tasks = deque(sorted([(x[1], x[0]) for x in jobs ], key= lambda x : (x[1], x[0])))
    q= []
    
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0,0
    while len(q) > 0 :
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        # 현재시간 + 실행시간 OR 요청시간 + 실행시간
        # 현재시간이 요청시간보다 더 클경우 뺄수없으므로 max !!! 
        
        total_response_time += current_time - arr
        # 요청 전 시간 빼기
        
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            # 현재시간보다 전의 작업들이 존재할때! 
            heapq.heappush(q, tasks.popleft())
            
        if len(tasks) > 0 and len(q) == 0:
            # 현재시간보다는 늦게 있지만, q가 존재하지않을때 (예외처리)
            heapq.heappush(q, tasks.popleft())
            
    return total_response_time // len(jobs)


def solution(jobs):
    answer = 0
    start = 0  #현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  #소요시간을 오름차순으로 정렬하기

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1: #전체 for문돌려서 start시점의 할당량없을경우 작업시간+1하기
                start += 1

    return answer // length
