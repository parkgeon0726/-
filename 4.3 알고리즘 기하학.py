#4.3 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/16931 문제
def surface_area(grid):
    n = len(grid)
    m = len(grid[0])
    area = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                # 상단과 하단 면적 (항상 2)
                area += 2
                # 4개의 측면 면적
                area += grid[i][j] * 4
                
                # 인접한 타워와 공유된 면적 빼기
                if i > 0:  # 위쪽 타워와의 공유면
                    area -= min(grid[i][j], grid[i-1][j]) * 2
                if j > 0:  # 왼쪽 타워와의 공유면
                    area -= min(grid[i][j], grid[i][j-1]) * 2     
    return area
# 입력 처리
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
# 결과 출력
print(surface_area(grid))

#https://www.acmicpc.net/problem/15973 문제
def determine_intersection_state(rect1, rect2):
    # 좌표 추출
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    # NULL 체크 (교차 없음)
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return "NULL"
    # POINT 체크 (한 점에서 만남)
    if (x2 == x3 and (y2 == y3 or y1 == y4)) or (x1 == x4 and (y2 == y3 or y1 == y4)) or \
       (y2 == y3 and (x2 == x3 or x1 == x4)) or (y1 == y4 and (x2 == x3 or x1 == x4)):
        return "POINT"
    # LINE 체크 (선분을 공유)
    if (x2 == x3 and y1 < y4 and y2 > y3) or (x1 == x4 and y1 < y4 and y2 > y3) or \
       (y2 == y3 and x1 < x4 and x2 > x3) or (y1 == y4 and x1 < x4 and x2 > x3):
        return "LINE"
    # 나머지는 모두 FACE (내부 영역 겹침)
    return "FACE"
# 입력 처리
rect1 = list(map(int, input().split()))
rect2 = list(map(int, input().split()))
# 결과 출력
print(determine_intersection_state(rect1, rect2))

#https://www.acmicpc.net/problem/16937 문제
import sys
h, w = map(int, input().split())  # 모눈종이의 크기
n = int(input())  # 스티커의 수
stickers = [list(map(int, input().split())) for _ in range(n)]  # 스티커 정보
result = 0  # 최대 넓이
for i in range(n):
    for j in range(i + 1, n):
        r1, c1 = stickers[i]  # 첫 번째 스티커
        r2, c2 = stickers[j]  # 두 번째 스티커
        area = r1 * c1 + r2 * c2  # 두 스티커의 넓이 합
        # 둘 다 회전하지 않는 경우
        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, area)
        # 첫 번째 스티커만 회전하는 경우
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            result = max(result, area)
        # 두 번째 스티커만 회전하는 경우
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            result = max(result, area)
        # 둘 다 회전하는 경우
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, area)
print(result)

#https://www.acmicpc.net/problem/16479 문제
def calculate_height_squared(K, D1, D2):
    # 반지름 차이 계산
    radius_diff = abs(D1 - D2) / 2
    # 피타고라스 정리를 이용하여 높이의 제곱 계산
    height_squared = K**2 - radius_diff**2
    return round(height_squared, 6)  # 10^-6까지 반올림
# 입력 받기
K = int(input())
D1, D2 = map(int, input().split())
# 높이의 제곱 계산 및 출력
result = calculate_height_squared(K, D1, D2)
# 정수인 경우와 실수인 경우를 구분하여 출력
if result == int(result):
    print(int(result))
else:
    print(result)

#https://www.acmicpc.net/problem/9240 문제
import sys
import math
# CCW(Counter-Clockwise) 함수: 세 점의 방향성을 판단
def ccw(p1, p2, p3):
    result = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if result > 0:
        return True  # 반시계 방향
    return False
# 두 점 사이의 거리 계산 함수
def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
def solve():
    C = int(input())
    # 화살이 2개면 바로 거리 계산
    if C == 2:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(math.sqrt(dist(a, b)))
        return
    # 화살 좌표 입력 및 정렬
    arrows = sorted([tuple(map(int, input().split())) for _ in range(C)])
    # 볼록 껍질의 아래 부분 계산
    convex_hull_down = []
    for i in range(C):
        while len(convex_hull_down) > 1:
            if ccw(convex_hull_down[-2], convex_hull_down[-1], arrows[i]):
                break
            convex_hull_down.pop()
        convex_hull_down.append(arrows[i])
    # 볼록 껍질의 위 부분 계산
    convex_hull_up = []
    for i in range(C - 1, -1, -1):
        while len(convex_hull_up) > 1:
            if ccw(convex_hull_up[-2], convex_hull_up[-1], arrows[i]):
                break
            convex_hull_up.pop()
        convex_hull_up.append(arrows[i])
    # 중복 제거한 볼록 껍질 완성
    hull = convex_hull_down[:-1] + convex_hull_up[:-1]
    # 볼록 껍질에서 가장 먼 거리 계산
    max_dist = 0
    n = len(hull)
    for i in range(n):
        for j in range(i+1, n):
            max_dist = max(max_dist, dist(hull[i], hull[j]))
    print(math.sqrt(max_dist))
if __name__ == "__main__":
    solve()


