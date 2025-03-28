#3.28 알고리즘 기하학 관련10문제

#https://www.acmicpc.net/problem/17387 문제
# CCW 함수 정의
#def ccw(x1, y1, x2, y2, x3, y3):
    # 외적을 이용하여 방향성을 계산
#    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
#    if result > 0:
#        return 1  # 반시계 방향
#    elif result < 0:
#        return -1  # 시계 방향
#    else:
#        return 0  # 일직선
# 선분 교차 여부 확인 함수
#def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # CCW 계산
#    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
#    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
#    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
#    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    # 두 선분이 서로 다른 방향으로 갈 경우 교차
#    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        # 선분이 일직선 상에 있을 경우 추가 확인
#        if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
            # 두 선분의 범위가 겹치는지 확인
#            if max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and \
#               max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2):
#                return True
#            else:
#                return False
#        return True
#    return False
# 입력 처리
#x1, y1, x2, y2 = map(int, input().split())
#x3, y3, x4, y4 = map(int, input().split())
# 결과 출력
#if is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
#    print(1)
#else:
#    print(0)

#https://www.acmicpc.net/problem/1708 문제
#def ccw(p1, p2, p3):
    # 외적을 이용한 방향성 계산
#    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
#def convex_hull(points):
    # 점들을 x좌표, y좌표 순으로 정렬
#    points = sorted(points)
    # 아래쪽 껍질 계산
#    lower = []
#    for point in points:
#        while len(lower) >= 2 and ccw(lower[-2], lower[-1], point) <= 0:
#            lower.pop()
#        lower.append(point)
    # 위쪽 껍질 계산
#    upper = []
#    for point in reversed(points):
#        while len(upper) >= 2 and ccw(upper[-2], upper[-1], point) <= 0:
#            upper.pop()
#        upper.append(point)
    # 아래쪽과 위쪽 껍질을 합치되, 마지막 점은 중복 제거
#    return lower[:-1] + upper[:-1]
# 입력 처리
#import sys
#input = sys.stdin.read
#data = input().splitlines()
#N = int(data[0])  # 점의 개수
#points = [tuple(map(int, line.split())) for line in data[1:]]
# 볼록 껍질 계산
#hull = convex_hull(points)
# 결과 출력: 볼록 껍질을 이루는 점의 개수
#print(len(hull))

#https://www.acmicpc.net/problem/2261 문제
import sys
import math
def closest_pair(points):
    def distance_squared(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    def brute_force(start, end):
        min_dist = float('inf')
        for i in range(start, end):
            for j in range(i + 1, end):
                min_dist = min(min_dist, distance_squared(points[i], points[j]))
        return min_dist
    def strip_closest(strip, d):
        min_dist = d
        strip.sort(key=lambda point: point[1])  # Sort by y-coordinate
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1])**2 >= min_dist:
                    break
                min_dist = min(min_dist, distance_squared(strip[i], strip[j]))
        return min_dist
    def closest_util(start, end):
        if end - start <= 3:
            return brute_force(start, end)
        mid = (start + end) // 2
        mid_x = points[mid][0]
        d_left = closest_util(start, mid)
        d_right = closest_util(mid, end)
        d = min(d_left, d_right)
        strip = [point for point in points[start:end] if abs(point[0] - mid_x)**2 < d]
        return min(d, strip_closest(strip, d))
    points.sort()  # Sort points by x-coordinate
    return closest_util(0, len(points))
# 입력 처리
input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
points = [tuple(map(int, line.split())) for line in data[1:]]
# 가장 가까운 두 점의 거리의 제곱 계산 및 출력
result = closest_pair(points)
print(result)

#https://www.acmicpc.net/problem/29751 문제
# 입력 받기
W, H = map(int, input().split())
# 삼각형 넓이 계산
area = (W * H) / 2
# 결과 출력 (소수점 아래 첫 번째 자리까지)
print(f"{area:.1f}")

#https://www.acmicpc.net/problem/17386 문제
def ccw(x1, y1, x2, y2, x3, y3):
    # CCW 계산
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # CCW 값 계산
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    # 두 선분이 서로 다른 방향에 있는지 확인
    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return 1
    # 일직선 상에 있는 경우 처리
    def is_between(a_x, a_y, b_x, b_y, c_x, c_y):
        # 점 C가 점 A와 B 사이에 있는지 확인
        return min(a_x, b_x) <= c_x <= max(a_x,b_x) and min(a_y,b_y)<=c_y<=max(a_y,b_y)
    if ccw1 == 0 and is_between(x1,y1,x2,y2,x3,y3): return 1
    if ccw2 == 0 and is_between(x1,y1,x2,y2,x4,y4): return 1
    if ccw3 == 0 and is_between(x3,y3,x4,y4,x1,y1): return 1
    if ccw4 == 0 and is_between(x3,y3,x4,y4,x2,y2): return 1
    # 교차하지 않는 경우
    return 0
# 입력 받기
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
# 결과 출력
print(is_intersect(x1,y1,x2,y2,x3,y3,x4,y4))

#https://www.acmicpc.net/problem/2162 문제
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.size = [1] * size  # 각 집합의 크기 저장
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # 랭크 기반 유니온
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.rank[root_x] += 1
    def group_size(self, x):
        return self.size[self.find(x)]
def ccw(x1, y1, x2, y2, x3, y3):
    # CCW 계산
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # 두 선분이 교차하거나 끝점에서 접촉하는지 확인
    def check_overlap(a1, a2, b):
        return min(a1, a2) <= b <= max(a1, a2)
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    # 일반적인 교차 조건
    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return True
    # 한 점에서 접촉하는 경우 처리
    if ccw1 == 0 and check_overlap(x1, x2, x3) and check_overlap(y1, y2, y3): return True
    if ccw2 == 0 and check_overlap(x1, x2, x4) and check_overlap(y1, y2, y4): return True
    if ccw3 == 0 and check_overlap(x3, x4, x1) and check_overlap(y3, y4, y1): return True
    if ccw4 == 0 and check_overlap(x3, x4, x2) and check_overlap(y3, y4, y2): return True
    return False
# 입력 처리
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
# Union-Find 초기화
uf = UnionFind(n)
# 모든 선분 쌍에 대해 교차 여부 확인 및 Union 수행
for i in range(n):
    for j in range(i + 1, n):
        if is_intersect(*segments[i], *segments[j]):
            uf.union(i, j)
# 결과 계산: 그룹 수와 가장 큰 그룹 크기
group_count = len(set(uf.find(i) for i in range(n)))
largest_group_size = max(uf.group_size(i) for i in range(n))
# 출력
print(group_count)
print(largest_group_size)

#https://www.acmicpc.net/problem/7510 문제
def is_right_triangle(a, b, c):
    # 피타고라스 정리 확인
    sides = sorted([a, b, c])  # 변을 정렬하여 가장 긴 변을 마지막으로 이동
    return sides[2]**2 == sides[0]**2 + sides[1]**2
# 입력 처리
n = int(input())  # 테스트 케이스 개수
results = []
for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    if is_right_triangle(a, b, c):
        results.append(f"Scenario #{i}:\nyes")
    else:
        results.append(f"Scenario #{i}:\nno")
# 출력 처리
print("\n\n".join(results))

#https://www.acmicpc.net/problem/1358 문제
def is_inside_rink(x, y, W, H, X, Y, px, py):
    # 반지름 계산
    R = H / 2
    # 직사각형 내부 확인
    if X <= px <= X + W and Y <= py <= Y + H:
        return True
    # 왼쪽 원 내부 확인
    if (px - X)**2 + (py - (Y + R))**2 <= R**2:
        return True
    # 오른쪽 원 내부 확인
    if (px - (X + W))**2 + (py - (Y + R))**2 <= R**2:
        return True
    return False
# 입력 처리
W, H, X, Y, P = map(int, input().split())
players = [tuple(map(int, input().split())) for _ in range(P)]
# 링크 안에 있는 선수 수 계산
count = sum(is_inside_rink(X, Y, W, H, X, Y, px, py) for px, py in players)
# 결과 출력
print(count)

#https://www.acmicpc.net/problem/2527 문제
import sys
input = sys.stdin.read
data = input().splitlines()
# 두 직사각형의 겹침 상태를 판별하는 함수
def classify_overlap(x1, y1, p1, q1, x2, y2, p2, q2):
    # 겹치는 영역의 좌표 계산
    overlap_x1 = max(x1, x2)  # 겹치는 영역의 왼쪽 아래 x좌표
    overlap_y1 = max(y1, y2)  # 겹치는 영역의 왼쪽 아래 y좌표
    overlap_x2 = min(p1, p2)  # 겹치는 영역의 오른쪽 위 x좌표
    overlap_y2 = min(q1, q2)  # 겹치는 영역의 오른쪽 위 y좌표
    # 공통부분이 없는 경우 (완전히 분리됨)
    if overlap_x1 > overlap_x2 or overlap_y1 > overlap_y2:
        return 'd'
    # 공통부분이 점인 경우
    if overlap_x1 == overlap_x2 and overlap_y1 == overlap_y2:
        return 'c'
    # 공통부분이 선분인 경우
    if overlap_x1 == overlap_x2 or overlap_y1 == overlap_y2:
        return 'b'
    # 공통부분이 직사각형인 경우
    return 'a'
# 입력 데이터 처리 및 출력
results = []
for line in data:
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, line.split())
    results.append(classify_overlap(x1, y1, p1, q1, x2, y2, p2, q2))
# 결과 출력
for result in results:
    print(result)

#https://www.acmicpc.net/problem/1064 문제
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def is_collinear(x1, y1, x2, y2, x3, y3):
    # 세 점이 일직선 상에 있는지 확인
    return (x2 - x1) * (y3 - y2) == (y2 - y1) * (x3 - x2)
def solve(xa, ya, xb, yb, xc, yc):
    # 세 점이 일직선 상에 있으면 평행사변형을 만들 수 없음
    if is_collinear(xa, ya, xb, yb, xc, yc):
        return -1.0
    # 세 점 사이의 거리 계산
    ab = distance(xa, ya, xb, yb)
    bc = distance(xb, yb, xc, yc)
    ca = distance(xc, yc, xa, ya)
    # 세 가지 방법으로 평행사변형 만들기
    # 각 평행사변형의 둘레는 인접한 두 변 길이의 합에 2를 곱한 값
    perimeter1 = ab + bc
    perimeter2 = bc + ca
    perimeter3 = ca + ab
    # 가장 큰 둘레와 가장 작은 둘레 찾기
    max_perimeter = max(perimeter1, perimeter2, perimeter3)
    min_perimeter = min(perimeter1, perimeter2, perimeter3)
    # 차이 반환 (둘레의 차이는 2 * (둘레의 절반의 차이))
    return 2 * (max_perimeter - min_perimeter)
# 입력 처리
xa, ya, xb, yb, xc, yc = map(int, input().split())
result = solve(xa, ya, xb, yb, xc, yc)
print(result)
