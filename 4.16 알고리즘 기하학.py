#4.16 알고리즘 기하학학 관련8문제

#https://www.acmicpc.net/problem/2536 문제
import sys
from collections import deque
  # 입력 처리
m, n = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
buses = []
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 좌표를 정규화: x1 <= x2, y1 <= y2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    elif x1 == x2 and y1 > y2:
        y1, y2 = y2, y1
    buses.append((b, x1, y1, x2, y2))
sx, sy, dx, dy = map(int, sys.stdin.readline().split())
  # 버스가 특정 교차점에 정차하는지 확인
def bus_stops_at(bus_idx, x, y):
    _, x1, y1, x2, y2 = buses[bus_idx]
    if x1 == x2:  # 수직 버스
        return x == x1 and y1 <= y <= y2
    else:  # 수평 버스 (y1 == y2)
        return y == y1 and x1 <= x <= x2
  # 두 버스가 공통 정류장을 가지는지 확인
def have_common_stop(i, j):
    _, x1a, y1a, x2a, y2a = buses[i]
    _, x1b, y1b, x2b, y2b = buses[j]
    # 두 버스 모두 수직
    if x1a == x2a and x1b == x2b:
        # 같은 수직선 상에 있어야 함
        if x1a == x1b:
            # y 범위가 겹치는지 확인
            return max(y1a, y1b) <= min(y2a, y2b)
        return False
    # 두 버스 모두 수평
    if y1a == y2a and y1b == y2b:
        # 같은 수평선 상에 있어야 함
        if y1a == y1b:
            # x 범위가 겹치는지 확인
            return max(x1a, x1b) <= min(x2a, x2b)
        return False
    # 하나는 수직, 하나는 수평
    if x1a == x2a:  # i는 수직, j는 수평
        # 교차점이 있고 그 교차점이 두 버스의 경로 내에 있는지 확인
        return x1b <= x1a <= x2b and y1a <= y1b <= y2a
    else:  # i는 수평, j는 수직
        # 교차점이 있고 그 교차점이 두 버스의 경로 내에 있는지 확인
        return x1a <= x1b <= x2a and y1b <= y1a <= y2b
  # 출발지와 목적지에 정차하는 버스 찾기
start_buses = []
dest_buses = []
for i in range(k):
    if bus_stops_at(i, sx, sy):
        start_buses.append(i)
    if bus_stops_at(i, dx, dy):
        dest_buses.append(i)
  # BFS로 최소 버스 수 찾기
visited = [False] * k
queue = deque([(bus, 1) for bus in start_buses])  # (버스 인덱스, 버스 수)
for bus in start_buses:
    visited[bus] = True
result = -1
while queue:
    bus, num_buses = queue.popleft()
    if bus in dest_buses:
        result = num_buses
        break
    for next_bus in range(k):
        if not visited[next_bus] and have_common_stop(bus, next_bus):
            visited[next_bus] = True
            queue.append((next_bus, num_buses + 1))
print(result)

#https://www.acmicpc.net/problem/14400 문제
import sys
# 입력 빠르게 받기
input = sys.stdin.readline
# 고객 수 입력
n = int(input())
# x좌표와 y좌표 따로 저장
x_coords = []
y_coords = []
for _ in range(n):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)
# 정렬하여 중앙값 찾기
x_coords.sort()
y_coords.sort()
# 중앙값 (인덱스는 0부터 시작하므로 n//2 사용)
x_mid = x_coords[n//2]
y_mid = y_coords[n//2]
# 모든 고객과의 거리 합 계산
total_distance = 0
for i in range(n):
    total_distance += abs(x_coords[i] - x_mid) + abs(y_coords[i] - y_mid)
print(total_distance)

#https://www.acmicpc.net/problem/10473 문제
import math
import heapq
def calculate_time(x1, y1, x2, y2, use_cannon):
    # 두 점 사이의 거리 계산
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # 그냥 걷는 시간
    walk_time = distance / 5
    # 대포를 사용할 수 있는 경우
    if use_cannon:
        # 대포로 50m 발사 후 남은 거리를 걷는 시간
        cannon_time = 2 + abs(distance - 50) / 5
        return min(walk_time, cannon_time)
    else:
        return walk_time
def find_shortest_time(start_x, start_y, end_x, end_y, cannons):
    # 모든 노드 (시작점, 대포들, 도착점)
    nodes = [(start_x, start_y)] + cannons + [(end_x, end_y)]
    n = len(nodes)
    # 그래프 구성 (인접 행렬) - 수정된 부분
    graph = [[0] * n for _ in range(n)]
    # 각 노드 쌍 사이의 이동 시간 계산
    for i in range(n):
        for j in range(n):
            if i != j:
                # 시작점(i=0)에서는 대포를 사용할 수 없음
                use_cannon = i != 0
                x1, y1 = nodes[i]
                x2, y2 = nodes[j]
                graph[i][j] = calculate_time(x1, y1, x2, y2, use_cannon)
    # 다익스트라 알고리즘
    # 시작점에서 각 노드까지의 최단 시간 - 수정된 부분
    times = [float('inf')] * n
    times[0] = 0  # 시작점의 시간은 0으로 설정
    # (시간, 노드) 형태의 우선순위 큐
    pq = [(0, 0)]
    while pq:
        current_time, current_node = heapq.heappop(pq)
        # 이미 더 빠른 경로를 찾았다면 무시
        if current_time > times[current_node]:
            continue
        # 인접 노드 탐색
        for neighbor in range(n):
            if neighbor != current_node:
                # 새로운 시간 = 현재까지의 시간 + 이동 시간
                new_time = current_time + graph[current_node][neighbor]
                
                # 더 빠른 경로를 발견했다면 업데이트
                if new_time < times[neighbor]:
                    times[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
    # 도착점(마지막 노드)까지의 최단 시간 반환
    return times[-1]
# 메인 함수
def main():
    # 입력 처리
    start_x, start_y = map(float, input().split())
    end_x, end_y = map(float, input().split())
    n = int(input())
    cannons = []
    for _ in range(n):
        x, y = map(float, input().split())
        cannons.append((x, y))
    # 최단 시간 계산 및 출력
    shortest_time = find_shortest_time(start_x, start_y, end_x, end_y, cannons)
    print(shortest_time)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/3878 문제
import sys
input = sys.stdin.readline
# CCW(Counter-Clockwise) 알고리즘
def ccw(p1, p2, p3):
    cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if cross_product > 0: return 1
    elif cross_product < 0: return -1
    else: return 0
# 점이 선분 위에 있는지 확인
def is_point_on_segment(point, segment):
    p1, p2 = segment
    if ccw(p1, p2, point) != 0:
        return False
    return min(p1[0], p2[0]) <= point[0] <= max(p1[0], p2[0]) and \
           min(p1[1], p2[1]) <= point[1] <= max(p1[1], p2[1])
# 선분 교차 판별
def is_intersect(line1, line2):
    p1, p2 = line1
    p3, p4 = line2
    ccw1 = ccw(p1, p2, p3)
    ccw2 = ccw(p1, p2, p4)
    ccw3 = ccw(p3, p4, p1)
    ccw4 = ccw(p3, p4, p2)
    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        return min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and \
               min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1])
    return ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0
# 볼록 껍질(Convex Hull) 구하기
def convex_hull(points):
    if len(points) <= 2:
        return points
    points.sort()
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
# 점이 볼록 다각형 내부에 있는지 판별
def is_point_inside_convex(point, polygon):
    n = len(polygon)
    if n <= 2:
        if n == 1:
            return point == polygon[0]
        if n == 2:
            return is_point_on_segment(point, (polygon[0], polygon[1]))
        return False
    for i in range(n):
        if is_point_on_segment(point, (polygon[i], polygon[(i+1) % n])):
            return True
    sign = None
    for i in range(n):
        c = ccw(polygon[i], polygon[(i+1) % n], point)
        if c == 0:
            continue
        if sign is None:
            sign = c
        elif sign * c < 0:
            return False
    return True
# 두 볼록 껍질이 겹치는지 확인
def is_hulls_overlap(hull1, hull2):
    n1, n2 = len(hull1), len(hull2)
    if n1 <= 2 or n2 <= 2:
        for p1 in hull1:
            for p2 in hull2:
                if p1 == p2:
                    return True
        if n1 == 2 and n2 == 1:
            return is_point_on_segment(hull2[0], (hull1[0], hull1[1]))
        if n1 == 1 and n2 == 2:
            return is_point_on_segment(hull1[0], (hull2[0], hull2[1]))
        if n1 == 2 and n2 == 2:
            return is_intersect((hull1[0], hull1[1]), (hull2[0], hull2[1]))
    for p in hull1:
        if is_point_inside_convex(p, hull2):
            return True
    for p in hull2:
        if is_point_inside_convex(p, hull1):
            return True
    for i in range(n1):
        for j in range(n2):
            if is_intersect((hull1[i], hull1[(i+1) % n1]), (hull2[j], hull2[(j+1) % n2])):
                return True
    return False
# 메인 함수
def solve():
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().strip().split())
        black_points = []
        for _ in range(n):
            x, y = map(int, input().strip().split())
            black_points.append((x, y))
        white_points = []
        for _ in range(m):
            x, y = map(int, input().strip().split())
            white_points.append((x, y))
        black_hull = convex_hull(black_points)
        white_hull = convex_hull(white_points)
        if is_hulls_overlap(black_hull, white_hull):
            print("NO")
        else:
            print("YES")
if __name__ == "__main__":
    solve()

#https://www.acmicpc.net/problem/11664 문제
import math
def distance(p1, p2):
    return math.sqrt(sum((a-b)**2 for a, b in zip(p1, p2)))
def min_distance_point_to_segment(A, B, C):
    # 벡터 AB
    AB = [B[0]-A[0], B[1]-A[1], B[2]-A[2]]
    # 벡터 AC
    AC = [C[0]-A[0], C[1]-A[1], C[2]-A[2]]
    # 벡터 AB의 길이의 제곱
    AB_squared = sum(x**2 for x in AB)
    # 벡터 AB와 AC의 내적
    AB_dot_AC = sum(a*b for a, b in zip(AB, AC))
    # 내적 / AB의 길이의 제곱 = 벡터 AB에 대한 AC의 사영 비율
    projection_ratio = AB_dot_AC / AB_squared
    if projection_ratio <= 0:
        # 사영점이 A보다 앞에 있는 경우
        return distance(A, C)
    elif projection_ratio >= 1:
        # 사영점이 B보다 뒤에 있는 경우
        return distance(B, C)
    else:
        # 사영점이 선분 AB 위에 있는 경우
        projection_point = [A[i] + projection_ratio * AB[i] for i in range(3)]
        return distance(projection_point, C)
# 입력 받기
Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())
A = (Ax, Ay, Az)
B = (Bx, By, Bz)
C = (Cx, Cy, Cz)
min_dist = min_distance_point_to_segment(A, B, C)
print("{:.10f}".format(min_dist))


#https://www.acmicpc.net/problem/4225 문제
import math
def ccw(p1, p2, p3):
    # 벡터의 외적으로 방향 계산
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
def convex_hull(points):
    # Graham's scan 알고리즘으로 볼록 껍질 구하기
    if len(points) <= 2:
        return points
    # y좌표가 가장 작은 점을 찾고, 같다면 x좌표가 작은 점 선택
    pivot = min(points, key=lambda p: (p[1], p[0]))
    # 각도 계산 함수
    def get_angle(p):
        if p == pivot:
            return float('-inf')
        return math.atan2(p[1] - pivot[1], p[0] - pivot[0])
    # 각도 기준 정렬
    sorted_points = sorted(points, key=lambda p: (get_angle(p), (p[0] - pivot[0])**2 + (p[1] - pivot[1])**2))
    # Graham's scan
    hull = [sorted_points[0], sorted_points[1]]
    for i in range(2, len(sorted_points)):
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], sorted_points[i]) <= 0:
            hull.pop()
        hull.append(sorted_points[i])
    return hull
def point_to_line_distance(point, line_p1, line_p2):
    # 점과 직선 사이의 거리 계산
    if line_p1 == line_p2:
        return math.sqrt((point[0] - line_p1[0])**2 + (point[1] - line_p1[1])**2)
    # 선분의 길이 제곱
    line_length_sq = (line_p2[0] - line_p1[0])**2 + (line_p2[1] - line_p1[1])**2
    # 외적을 이용한 거리 계산
    return abs(ccw(line_p1, line_p2, point)) / math.sqrt(line_length_sq)
def min_width(hull):
    n = len(hull)
    if n <= 2:
        return 0
    min_width_val = float('inf')
    # 각 변에 대해 최대 거리 계산
    for i in range(n):
        max_dist = 0
        for j in range(n):
            dist = point_to_line_distance(hull[j], hull[i], hull[(i + 1) % n])
            max_dist = max(max_dist, dist)
        min_width_val = min(min_width_val, max_dist)
    return min_width_val
def main():
    case = 1
    while True:
        n = int(input())
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        # 볼록 껍질 구하기
        hull = convex_hull(points)
        # 최소 너비 계산
        width = min_width(hull)
        # 0.01 단위로 올림
        width = math.ceil(width * 100) / 100
        print(f"Case {case}: {width:.2f}")
        case += 1
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/11662 문제
import math
def minho_position(p, Ax, Ay, Bx, By):
    # p% 만큼 이동했을 때 민호의 위치
    x = Ax + (Bx - Ax) * (p / 100)
    y = Ay + (By - Ay) * (p / 100)
    return [x, y]
def kangho_position(p, Cx, Cy, Dx, Dy):
    # p% 만큼 이동했을 때 강호의 위치
    x = Cx + (Dx - Cx) * (p / 100)
    y = Cy + (Dy - Cy) * (p / 100)
    return [x, y]
def distance(pos1, pos2):
    # 두 점 사이의 거리 계산
    return math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)
# 입력 받기
Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(float, input().split())
# 초기 최소 거리(문제 조건에 따른 최대 가능 거리로 설정)
min_dist = math.sqrt(10000**2 + 10000**2)
# 삼분 탐색을 위한.초기 구간 설정
left = 0
right = 100
# 요구되는 정밀도에 도달할 때까지 삼분 탐색 진행
while right - left >= 1e-7:  # 10^-6 오차 허용을 위해 10^-7까지 탐색
    # 두 개의 중간점 계산
    mid1 = left + (right - left) / 3
    mid2 = right - (right - left) / 3
    # 중간점에서의 위치 계산
    pos_minho_mid1 = minho_position(mid1, Ax, Ay, Bx, By)
    pos_kangho_mid1 = kangho_position(mid1, Cx, Cy, Dx, Dy)
    pos_minho_mid2 = minho_position(mid2, Ax, Ay, Bx, By)
    pos_kangho_mid2 = kangho_position(mid2, Cx, Cy, Dx, Dy)
    # 중간점에서의 거리 계산
    dist_mid1 = distance(pos_minho_mid1, pos_kangho_mid1)
    dist_mid2 = distance(pos_minho_mid2, pos_kangho_mid2)
    # 최소 거리 업데이트
    min_dist = min(min_dist, dist_mid1, dist_mid2)
    # 탐색 구간 조정
    if dist_mid1 > dist_mid2:
        # 최소값이 mid1과 right 사이에 있음
        left = mid1
    else:
        # 최소값이 left와 mid2 사이에 있음
        right = mid2
# 정밀도에 맞게 결과 출력
print("{:.10f}".format(min_dist))

#https://www.acmicpc.net/problem/16485 문제
def solve():
    c, b = map(int, input().split())
    result = c / b  # 실수 나눗셈 사용
    print(result)
solve()
