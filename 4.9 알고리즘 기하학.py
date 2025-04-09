#4.9 알고리즘 기하학 5문제

#https://www.acmicpc.net/problem/12781 문제
def ccw(x1, y1, x2, y2, x3, y3):
    """세 점의 방향 관계를 판단하는 CCW 알고리즘"""
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
def pizza_alvoloc(points):
    """두 선분이 교차하는지 판단하여 피자가 4조각으로 나눠지는지 확인"""
    x1, y1, x2, y2, x3, y3, x4, y4 = points
    # 선분 1-2에 대한 점 3과 점 4의 방향 관계
    a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    # 선분 3-4에 대한 점 1과 점 2의 방향 관계
    b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    # 두 값이 모두 음수이면 선분이 교차
    return 1 if a < 0 and b < 0 else 0
# 입력 처리
points = list(map(int, input().split()))
# 결과 출력
print(pizza_alvoloc(points))

#https://www.acmicpc.net/problem/3108 문제
def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def is_overlapping(rect1, rect2):
    x1_1, y1_1, x2_1, y2_1 = rect1
    x1_2, y1_2, x2_2, y2_2 = rect2
    # 한 직사각형이 다른 직사각형 내부에 완전히 포함되는 경우
    if (x1_1 < x1_2 and y1_1 < y1_2 and x2_1 > x2_2 and y2_1 > y2_2) or \
       (x1_2 < x1_1 and y1_2 < y1_1 and x2_2 > x2_1 and y2_2 > y2_1):
        return False
    # 겹치지 않는 경우
    if x2_1 < x1_2 or x1_1 > x2_2 or y2_1 < y1_2 or y1_1 > y2_2:
        return False
    # 겹치는 경우
    return True
def is_origin_on_rect_border(rect):
    x1, y1, x2, y2 = rect
    # 원점이 직사각형의 테두리에 있는 경우
    return (x1 == 0 and y1 <= 0 <= y2) or (x2 == 0 and y1 <= 0 <= y2) or \
           (y1 == 0 and x1 <= 0 <= x2) or (y2 == 0 and x1 <= 0 <= x2)
def solution():
    n = int(input())
    rectangles = []
    parent = list(range(n))
    # 원점이 직사각형의 테두리에 있는지 확인
    origin_border_rect = -1
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append((x1, y1, x2, y2))
        if is_origin_on_rect_border(rectangles[i]):
            if origin_border_rect == -1:
                origin_border_rect = i
            else:
                union_parent(parent, origin_border_rect, i)
    # 직사각형 간의 관계 확인
    for i in range(n):
        for j in range(i+1, n):
            if is_overlapping(rectangles[i], rectangles[j]):
                union_parent(parent, i, j)
    # 연결된 집합의 개수 계산
    groups = set()
    for i in range(n):
        groups.add(find_parent(parent, i))
    # 필요한 PU 명령의 횟수 계산
    if origin_border_rect != -1:
        # 원점이 직사각형의 테두리에 있는 경우 해당 집합은 PU 필요 없음
        return len(groups) - 1
    else:
        # 원점이 직사각형의 테두리에 없는 경우 모든 집합이 PU 필요
        return len(groups)
print(solution())

#https://www.acmicpc.net/problem/9772 문제
def determine_quadrant(x, y):
    if x == 0 or y == 0:
        return "AXIS"
    elif x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"
while True:
    x, y = map(float, input().split())
    print(determine_quadrant(x, y))
    if x == 0 and y == 0:
        break

#https://www.acmicpc.net/problem/10254 문제 (시간초과문제로 통과를 못함함)
def find_farthest_points(points):
    # 컨벡스 헐 계산
    def ccw(p1, p2, p3):
        return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])
    # 점들을 x좌표 기준으로 정렬
    points.sort()
    # 하단 헐 계산
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    # 상단 헐 계산
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # 컨벡스 헐 완성 (중복 제거)
    hull = lower[:-1] + upper[:-1]
    # 가장 먼 두 점 찾기
    max_dist, result = 0, (hull[0], hull[0])
    for i in range(len(hull)):
        for j in range(i+1, len(hull)):
            d = (hull[i][0]-hull[j][0])**2 + (hull[i][1]-hull[j][1])**2
            if d > max_dist:
                max_dist, result = d, (hull[i], hull[j])
    return result
# 테스트 케이스 처리
for _ in range(int(input())):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    p1, p2 = find_farthest_points(points)
    print(p1[0], p1[1], p2[0], p2[1])

#https://www.acmicpc.net/problem/7869 문제
import math
# 입력 받기
x1, y1, r1, x2, y2, r2 = map(float, input().split())
# 중심 간 거리 계산
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# 경우 1: 교차하지 않는 경우
if d >= r1 + r2:
    answer = 0
# 경우 2: 하나의 원이 다른 원 내부에 완전히 포함된 경우
elif d <= abs(r1 - r2):
    answer = math.pi * min(r1, r2)**2
# 경우 3: 부분적으로 교차하는 경우
else:
    # 각도 계산 (코사인 법칙 사용, 안정성 보장)
    cos_angle1 = (d**2 + r1**2 - r2**2) / (2 * d * r1)
    cos_angle1 = max(-1, min(1, cos_angle1))  # 부동소수점 오차 방지
    angle1 = 2 * math.acos(cos_angle1)
    cos_angle2 = (d**2 + r2**2 - r1**2) / (2 * d * r2)
    cos_angle2 = max(-1, min(1, cos_angle2))  # 부동소수점 오차 방지
    angle2 = 2 * math.acos(cos_angle2)
    # 부채꼴 넓이 계산
    sector_area1 = 0.5 * r1**2 * (angle1 - math.sin(angle1))
    sector_area2 = 0.5 * r2**2 * (angle2 - math.sin(angle2))
    # 총 교차 영역 넓이
    answer = sector_area1 + sector_area2
# 출력 (소수점 셋째 자리까지)
print("{:.3f}".format(answer))
