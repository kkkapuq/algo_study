def solution(clothes):
    # 1. 결괏값과 해시맵 선언
    result = 1
    hash_map = dict()
    
    # 2. 의상을 종류별로 구분하기
    for wear, kind in clothes:
        # 3. get method로 1씩 증가, 없다면 0 삽입
        hash_map[kind] = hash_map.get(kind, 0) + 1
        
    # 3. 모든 조합 계산하기( 입지 않는 경우 포함 )
    for kind in hash_map:
        result *= (hash_map[kind] + 1)
    
    # 4. 아무종류의 옷도 입지 않는 경우를 제외한 값 반환
    return result - 1