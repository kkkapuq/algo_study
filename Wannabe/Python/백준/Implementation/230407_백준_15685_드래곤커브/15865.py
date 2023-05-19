from collections import defaultdict
import sys
from typing import *
si = sys.stdin.readline

# dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]            # ENWS
dir_op = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# 90 deg is to add -1 to idx




def store_state(curve_id, start, x, y, hist):
    # hist를 따라가면서 새롭게 도착하는 좌표를 저장하는 함수
    # start : 시작인덱스, 가장 최근 세대의 끝지점을 나타내는 순서 인덱스
    # x, y : 시작점, 가장 최근 세대-1 의 끝 지점과 같다
    # hist : 정수로 주어진 문자열 , 해당하는 드래곤커브가 세대를 지나며 이동한 가장 최근 기록이다
    new_track = transform(hist)
    ix, iy = x, y
    for way in new_track[start+1:]:                 # start 다음부터 방향전환에 따른다
        ix += dir_op[way][0]
        iy += dir_op[way][1]
        # store에 저장을 하면서 이 드래곤 커브는 점을 소유한다.
        curve[curve_id].append((ix, iy))


def transform(curve_id, hist):
    # 지금까지 이동해온 방향순서를 거꾸로 순회하면서 90도 회전하는 코드
    new_dir = []
    for d in hist[::-1]:
        new_dir.append((d-1)%4)
    curve[curve_id] = hist+new_dir
    return hist+new_dir

def init_vector(curve_id, x, y, d, hist):
    # 초기 방향 세팅 및 hist 기록
    curve[curve_id].append((x, y))
    rx = x+dir_op[d][0]
    ry = y+dir_op[d][1]
    hist[curve_id].append(d)
    return rx, ry


N = int(si().strip())
curve = [[] for _ in range(N+1)]
hist = [[] for _ in range(N+1)]


for i in range(N):
    x, y, d, g = map(int, si().strip().split())        # 시작점 (x, y) 방향, 세대(반복)
    ix, iy = init_vector(i, x, y, d)
    for _ in range(g):
        store_state(i, 0, ix, iy, hist[i])