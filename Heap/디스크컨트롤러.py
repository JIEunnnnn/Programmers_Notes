#LV.3 디스크컨트롤러
#소요시간을 최소화하여 반환하기 
#
#힙구조로만 생각했는데, 2중포문돌려서 start를 더함으로써 구하는 방식도 있다는걸알게됨...ㄷㄷ 
#

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
