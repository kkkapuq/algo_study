def solution(cap, n, deliveries, pickups):
    answer = 0
    # 0. n = 100,000 이라 완탐은 안됨, 그리디 문제
    # 1. 일단, 한번에 멀리 나가야 동선이 최적화 되므로, 먼곳부터 탐색하도록 한다.
    # 다른거 다 필요없음. 이 집을 비우는데 얼만큼의 거리가 소모되는가? 로 계산하자.
    
    d, p = 0, 0
    
    for i in range(n-1, -1, -1):
        # 배달항목과 수거항목
        # i번째 집을 들를 때 기존 짐과 더불어 배송/수거해야 하는 양이다.
        d += deliveries[i]
        p += pickups[i]
        
        # 만약, 배송/수거 해야하는게 남아있다면, 어차피 나는 물류센터 갔다가 여길 다시 와야된다.
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i+1)*2
            
            
    return answer