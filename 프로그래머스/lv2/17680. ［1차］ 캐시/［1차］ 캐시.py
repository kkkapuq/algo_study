# 캐시에 들어있는 도시를 제외한 나머지 도시들의 참조시간을 업데이트 해주는 함수
def refreshTime(city, cache):
    for key, value in cache.items():
        if city != key:
            cache[key] += 1
    return cache

def solution(cacheSize, cities):
    answer = 0
    # LRU = 가장 오랫동안 사용되지 않은 캐시를 제거
    # 1. cache를 도시 : 참조시간 으로 이뤄진 딕셔너리 형태로 선언한다.
    cache = {}
    
    # cacheSize가 0이면 걍 싹 다 cache miss
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        # 대소문자 구분이 없으므로, 전부 lower 처리해준다.
        city = city.lower()
        # 2. 캐시 사이즈 미만이고, 캐시 안에 도시가 없다면 그냥 넣어준다.
        if len(cache) < cacheSize and city not in cache:
            cache[city] = 0
            answer += 5
            cache = refreshTime(city, cache)
            # 2-1. city가 캐시 안에 있다면 시간을 갱신해준다.
        elif city in cache:
            cache[city] = 0
            answer += 1
            cache = refreshTime(city, cache)
        # 3. cache 사이즈가 초과된 상태고, 안에 city가 없다면 LRU를 실행해준다.
        else:
            maxTime = 0
            changedCity = ''
            for key, value in cache.items():
                maxTime = max(maxTime, value)
                if maxTime == value:
                    changedCity = key
            del cache[changedCity]
            cache[city] = 0
            cache = refreshTime(city, cache)
            answer += 5
    
    return answer