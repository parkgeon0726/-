#4.10 알고리즘 기하학 5문제

#https://www.acmicpc.net/problem/25308 문제
from itertools import permutations
def is_convex(arr):
    n = len(arr)
    for i in range(n):
        x, y, z = arr[i], arr[(i + 1) % n], arr[(i + 2) % n]
        if (x + z) * (x + z) * y * y < 2 * x * x * z * z:
            return False
    return True
def count_convex_permutations(abilities):
    count = 0
    for perm in permutations(abilities):
        if is_convex(perm):
            count += 1
    return count
# 입력 받기
abilities = list(map(int, input().split()))
result = count_convex_permutations(abilities)
print(result)

#https://www.acmicpc.net/problem/7420 문제
import math
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def convex_hull(points):
    # x좌표 기준으로 정렬
    points = sorted(points)
    lower = []
    # 아래쪽 껍질 구하기
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    # 위쪽 껍질 구하기
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # 중복되는 시작점과 끝점을 제외하고 합치기
    return lower[:-1] + upper[:-1]
def calculate_perimeter(hull):
    perimeter = 0
    for i in range(len(hull)):
        perimeter += calculate_distance(hull[i], hull[(i + 1) % len(hull)])
    return perimeter
def solve_problem(n, l, coordinates):
    hull = convex_hull(coordinates)
    perimeter = calculate_perimeter(hull)
    # 방벽의 길이 = 컨벡스 헐의 둘레 + 2 * π * L
    expanded_perimeter = perimeter + 2 * math.pi * l
    return round(expanded_perimeter)
# 입력 받기
n, l = map(int, input().split())
coordinates = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))
# 결과 출력
result = solve_problem(n, l, coordinates)
print(result)

#https://www.acmicpc.net/problem/15923 문제
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
perimeter = 0
for i in range(n):
    next_i = (i + 1) % n
    dx = abs(points[i][0] - points[next_i][0])
    dy = abs(points[i][1] - points[next_i][1])
    perimeter += dx + dy
print(perimeter)

#https://www.acmicpc.net/problem/3679 문제
import sys
from functools import cmp_to_key
input = sys.stdin.readline
def ccw(a, b, c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])
def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2
def cmp(a, b):
    global ref
    if ccw(ref, a, b) > 0:
        return 1
    if ccw(ref, a, b) == 0 and dist(ref, a) > dist(ref, b):
        return 1
    return -1
def solve():
    global ref
    N, *raw = map(int, input().split())
    points = list()
    ref = (10001, 10001, -1)
    for i in range(N):
        p = (raw[2*i], raw[2*i+1], i)
        points.append(p)
        if ref > p:  # x좌표가 작은 점을 기준점으로 선택
            ref = p
    points.sort(key=cmp_to_key(cmp))
    last, last_ref = list(), points[-1]
    ans = [ref]
    for p in points:
        if p == ref:
            continue
        if ccw(ref, last_ref, p) == 0:
            last.append(p)  # 마지막 점과 같은 직선 상에 있는 점들
        else:
            ans.append(p)
    last.reverse()  # 같은 직선 상의 점들은 거리 순서 반대로
    print(*[p[2] for p in ans+last])
# 입력 처리
c = int(input())
for _ in range(c):
    solve()

#https://www.acmicpc.net/problem/21335 문제
from math import pi
# 가스가 덮은 면적 입력
a = int(input())
# 반지름 계산: r = √(a/π)
r = (a / pi) ** 0.5
# 둘레 계산: C = 2πr
c = 2 * pi * r
# 결과 출력
print(c)
