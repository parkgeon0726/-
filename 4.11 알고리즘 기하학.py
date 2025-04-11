#4.11 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/11880 문제
from sys import stdin
# 테스트 케이스 수 입력
T = int(stdin.readline())
# 각 테스트 케이스에 대해 처리
for _ in range(T):
    # 지우개의 가로, 세로, 높이 입력
    a, b, c = map(int, stdin.readline().split())
    # 가장 긴 변 찾기
    max_length = max(a, b, c)
    # 최단 거리의 제곱 계산
    shortest_squared = (a + b + c - max_length) ** 2 + max_length ** 2
    # 결과 출력
    print(shortest_squared)

#https://www.acmicpc.net/problem/1198 문제
import sys
from itertools import combinations
# 입력 받기
n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
# 삼각형의 넓이 계산 함수
def calculate_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
# 모든 가능한 3개 점의 조합을 고려하여 최대 넓이 찾기
max_area = 0
for p1, p2, p3 in combinations(points, 3):
    area = calculate_area(p1, p2, p3)
    if area > max_area:
        max_area = area
print(max_area)

#https://www.acmicpc.net/problem/17371 문제
import math
def distance(x1, y1, x2, y2):
    # 두 점 사이의 유클리드 거리를 계산
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def find_optimal_location():
    n = int(input())
    facilities = []
    # 편의시설 좌표 입력
    for _ in range(n):
        x, y = map(int, input().split())
        facilities.append((x, y))
    min_max_dist = float('inf')
    optimal_position = None
    # 각 편의시설에 대해 최댓값 계산
    for i, (x1, y1) in enumerate(facilities):
        max_dist = 0
        for j, (x2, y2) in enumerate(facilities):
            if i != j:  # 자기 자신 제외
                dist = distance(x1, y1, x2, y2)
                max_dist = max(max_dist, dist)
        # 최댓값 중 최솟값 찾기
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            optimal_position = (x1, y1)
    # 결과 출력
    print(optimal_position[0], optimal_position[1])
find_optimal_location()

#https://www.acmicpc.net/problem/1711 문제
import math
from collections import defaultdict
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
total = 0
for i in range(n):
    ax, ay = points[i]
    vectors = defaultdict(int)
    for j in range(n):
        if i == j:
            continue
        dx = points[j][0] - ax
        dy = points[j][1] - ay
        g = math.gcd(dx, dy)
        nx = dx // g
        ny = dy // g
        vectors[(nx, ny)] += 1
    current = 0
    for (x, y), cnt in vectors.items():
        perp = (-y, x)
        if perp in vectors:
            current += cnt * vectors[perp]
    total += current
print(total)

#https://www.acmicpc.net/problem/17247 문제
# 행과 열 크기 입력
n, m = map(int, input().split())
# 2차원 배열 입력
board = [list(map(int, input().split())) for _ in range(n)]
# 두 개의 1 위치 찾기
points = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            points.append((i, j))
            if len(points) == 2:  # 두 개의 1을 모두 찾으면 반복 종료
                break
    if len(points) == 2:
        break
# 택시 거리 계산
taxi_distance = abs(points[1][0] - points[0][0]) + abs(points[1][1] - points[0][1])
# 결과 출력
print(taxi_distance)
