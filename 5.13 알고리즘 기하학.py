#5.13 알고리즘기하학 관련5문제

#https://www.acmicpc.net/problem/6850 문제
import sys
def cross(p1, p2, p3):
    """세 점의 방향성을 판단하는 함수 (CCW)"""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
def compute_convex_hull(points):
    """모노톤 체인 알고리즘을 이용한 볼록 껍질 계산"""
    # 중복 제거
    points = list(set(points))
    if len(points) <= 2:
        return points
    # 좌표 순으로 정렬
    points.sort()
    # 아래쪽과 위쪽 껍질 구성
    lower = []
    upper = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # 중복 제거하여 반환
    return lower[:-1] + upper[:-1]
def polygon_area(vertices):
    """신발끈 공식을 이용한 다각형 면적 계산"""
    n = len(vertices)
    if n < 3:
        return 0
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
    return abs(area) / 2
def main():
    n = int(sys.stdin.readline().strip())
    if n <= 2:
        print(0)
        return
    points = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        points.append((x, y))
    hull = compute_convex_hull(points)
    area = polygon_area(hull)
    cows = int(area / 50)
    print(cows)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/3495 문제
# 도형의 높이와 너비 입력
h, w = map(int, input().split())
# 도형 정보 입력
grid = []
for i in range(h):
    grid.append(input())
dot_area = 0  # 내부의 '.' 문자가 차지하는 넓이
slash_count = 0  # '/' 또는 '\' 문자의 수
for i in range(h):
    inside = False  # 현재 위치가 도형 내부인지 여부
    for j in range(w):
        if grid[i][j] == '/' or grid[i][j] == '\\':
            slash_count += 1
            inside = not inside  # 경계를 만나면 내부/외부 상태 전환
        elif inside and grid[i][j] == '.':
            dot_area += 1  # 내부의 '.' 문자는 1의 넓이 추가
# 전체 넓이 계산: 내부 점의 넓이 + '/'와 '\' 문자들의 넓이
total_area = dot_area + (slash_count // 2)
print(total_area)

#https://www.acmicpc.net/problem/17286 문제
from itertools import permutations
import math
# 두 점 사이의 유클리드 거리 계산 함수
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
# 입력 받기
yumi = list(map(int, input().split()))
people = []
for _ in range(3):
    people.append(list(map(int, input().split())))
# 가능한 모든 방문 순서에 대해 최소 거리 계산
min_distance = float('inf')
for order in permutations([0, 1, 2]):
    current_pos = yumi
    total_distance = 0
    for i in order:
        total_distance += distance(current_pos, people[i])
        current_pos = people[i]
    min_distance = min(min_distance, total_distance)
# 소수점 이하는 버리고 정수만 출력
print(int(min_distance))

#https://www.acmicpc.net/problem/16480 문제
# 백준 16480번 문제: 외심과 내심은 사랑입니다
# 오일러의 정리 활용: OI² = R(R - 2r)
# 입력 받기
R, r = map(int, input().split())
# 외심과 내심 사이의 거리의 제곱 계산
distance_squared = R * (R - 2 * r)
# 결과 출력
print(distance_squared)

#https://www.acmicpc.net/problem/2121 문제
import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
points = set()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.add((x, y))
count = 0
for x, y in points:
    if ((x + a, y) in points and 
        (x, y + b) in points and 
        (x + a, y + b) in points):
        count += 1
print(count)
