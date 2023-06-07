'''
문제 : 신고 결과 받기
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92334
'''
def solution(id_list, report, k):
    answer = [ 0 for _ in range(len(id_list))]
    
    # 1. 이용자 id : 피신고자 id 형태로 map을 만들어주자
    reporterDic = {}
    for i in report:
        # 신고자, 피신고자
        reporter = i.split()[0]
        reportee = i.split()[1]
        
        if reporter not in reporterDic:
            reporterDic[reporter] = [reportee]
        # 1-1. 이 때, 중복신고는 무시한다.
        elif reporter in reporterDic:
            if reportee not in reporterDic[reporter]:
                reporterDic[reporter].append(reportee)
    
    # 2. 피신고자 id : 신고당한 횟수 형태로 map을 만들어준다.
    reporteeDic = {}
    banned = []
    for reportee in reporterDic.values():
        for i in reportee:
            if i not in reporteeDic:
                reporteeDic[i] = 1
            elif i in reporteeDic:
                reporteeDic[i] += 1
            # 3. 정지당한 사용자들의 id를 취합한다.
            if reporteeDic[i] >= k and i not in banned:
                banned.append(i)
        
    # 4. 1번에 있는 map을 순회하면서, 정지당한 사용자들의 id가 있으면 answer에 더해준다.
    for reporter, reportee in reporterDic.items():
        for i in reportee:
            if i in banned:
                answer[id_list.index(reporter)] += 1 
    
    return answer

