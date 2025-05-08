#5.8 알고리즘기하학 관련5문제

#https://www.acmicpc.net/problem/23375 문제
# 입력 받기
x, y = map(int, input().split())
r = int(input())
# 정사각형의 꼭짓점 좌표 계산 (시계방향)
print(x-r, y+r)  # 좌상단
print(x+r, y+r)  # 우상단
print(x+r, y-r)  # 우하단
print(x-r, y-r)  # 좌하단

#https://www.acmicpc.net/problem/2254 문제
def convex_hull(points):
    points = sorted(points)
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def is_inside(hull, px, py):
    n = len(hull)
    if n < 3:
        return False
    sign = None
    for i in range(n):
        a = hull[i]
        b = hull[(i+1) % n]
        current_ccw = (b[0] - a[0]) * (py - a[1]) - (b[1] - a[1]) * (px - a[0])
        if current_ccw == 0:
            return False
        current_sign = 1 if current_ccw > 0 else -1
        if sign is None:
            sign = current_sign
        else:
            if current_sign != sign:
                return False
    return True
n, px, py = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
remaining = points.copy()
answer = 0
while True:
    if len(remaining) < 3:
        break
    hull = convex_hull(remaining)
    if len(hull) < 3:
        break
    if not is_inside(hull, px, py):
        break
    answer += 1
    hull_set = set(hull)
    remaining = [p for p in remaining if p not in hull_set]
print(answer)

#https://www.acmicpc.net/problem/11466 문제
h, w = map(int, input().split())
a, b = max(h, w), min(h, w)
s1 = min(a / 3, b)
s2 = min(a / 2, b / 2)
print("{0:.3f}".format(max(s1, s2)))

#https://www.acmicpc.net/problem/2699 문제
def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

def convex_hull(points):
    # 점이 3개 미만인 경우 처리
    if len(points) <= 2:
        return sorted(points, key=lambda p: (-p[1], p[0]))
    
    # y좌표 반전 (일반적인 알고리즘 적용을 위해)
    inverted_points = [(x, -y) for x, y in points]
    
    # Graham scan
    inverted_points.sort()  # x값 오름차순, x값이 같으면 y값 오름차순
    
    lower = []
    for p in inverted_points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(inverted_points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    # 껍질 합치기 (중복 제거)
    inverted_hull = lower[:-1] + upper[:-1]
    
    # 원래 y좌표로 변환
    original_hull = [(x, -y) for x, y in inverted_hull]
    
    # y좌표가 가장 큰 점(동일하면 x좌표가 가장 작은 점)을 찾아 시작점으로
    start_idx = max(range(len(original_hull)), key=lambda i: (original_hull[i][1], -original_hull[i][0]))
    
    # 시작점부터 시계 방향으로 정렬
    result = []
    for i in range(len(original_hull)):
        result.append(original_hull[(start_idx + i) % len(original_hull)])
    
    return result

# 테스트 케이스 수 입력
P = int(input())

for _ in range(P):
    # 격자점 수 입력
    N = int(input())
    points = []
    
    # 격자점 좌표 입력 (한 줄에 최대 5개의 점)
    for _ in range((N + 4) // 5):
        line = list(map(int, input().split()))
        for i in range(0, len(line), 2):
            if i+1 < len(line) and len(points) < N:
                points.append((line[i], line[i+1]))
    
    # 컨벡스 헐 계산
    hull = convex_hull(points)
    
    # 결과 출력
    print(len(hull))
    for point in hull:
        print(point[0], point[1])


#https://www.acmicpc.net/problem/16958 문제
import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    
    n = int(input[idx])
    idx += 1
    T = int(input[idx])
    idx += 1
    
    cities = []
    specials = []
    
    for _ in range(n):
        s = int(input[idx])
        x = int(input[idx+1])
        y = int(input[idx+2])
        idx += 3
        cities.append((s, x, y))
        if s == 1:
            specials.append((x, y))
    
    near = [0] * n
    for i in range(n):
        if cities[i][0] == 1:
            near[i] = 0
        else:
            min_dist = float('inf')
            for (x_s, y_s) in specials:
                dist = abs(cities[i][1] - x_s) + abs(cities[i][2] - y_s)
                if dist < min_dist:
                    min_dist = dist
            near[i] = min_dist
    
    m = int(input[idx])
    idx += 1
    
    output = []
    for _ in range(m):
        a = int(input[idx]) - 1
        b = int(input[idx+1]) - 1
        idx += 2
        
        direct = abs(cities[a][1] - cities[b][1]) + abs(cities[a][2] - cities[b][2])
        if not specials:
            output.append(direct)
            continue
        
        tele = near[a] + T + near[b]
        output.append(min(direct, tele))
    
    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()
