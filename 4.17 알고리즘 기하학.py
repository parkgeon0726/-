#4.17 알고리즘기하학 관련5문제

#https://www.acmicpc.net/problem/16478 문제
a, b, c = map(int, input().split())
result = (a * c) / b
print("{0:.10g}".format(result))

#https://www.acmicpc.net/problem/5620 문제
import sys
import bisect
import math
def closest_pair(points):
    points.sort()
    return closest_pair_recursive(points, 0, len(points) - 1)
def closest_pair_recursive(points, start, end):
    if end - start <= 3:
        return brute_force(points, start, end)
    mid = (start + end) // 2
    mid_x = points[mid][0]
    left_min = closest_pair_recursive(points, start, mid)
    right_min = closest_pair_recursive(points, mid + 1, end)
    min_dist = min(left_min, right_min)
     # bisect를 이용한 효율적인 스트립 구성
    sqrt_d = int(math.isqrt(min_dist)) if min_dist > 0 else 0
    low_x = mid_x - sqrt_d
    high_x = mid_x + sqrt_d
    left_idx = bisect.bisect_left(points, (low_x, -float('inf')), start, end + 1)
    right_idx = bisect.bisect_right(points, (high_x, float('inf')), start, end + 1)
    strip = []
    for i in range(left_idx, right_idx):
        dx = points[i][0] - mid_x
        if dx * dx < min_dist:
            strip.append(points[i])
    # strip을 y좌표 기준으로 정렬
    strip.sort(key=lambda p: p[1])
    # 각 점에 대해 최대 6개 점만 검사 (거리 계산 최적화)
    strip_len = len(strip)
    for i in range(strip_len):
        for j in range(i + 1, min(i + 7, strip_len)):
            dy = strip[j][1] - strip[i][1]
            if dy * dy >= min_dist:
                break
            current_dist = (strip[i][0] - strip[j][0])**2 + dy**2
            if current_dist < min_dist:
                min_dist = current_dist
    return min_dist
def brute_force(points, start, end):
    min_dist = float('inf')
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = dx * dx + dy * dy
            if dist < min_dist:
                min_dist = dist
    return min_dist
def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    points = []
    idx = 1
    for _ in range(n):
        x, y = int(input[idx]), int(input[idx+1])
        points.append((x, y))
        idx += 2
    if n == 2:
        dx = points[0][0] - points[1][0]
        dy = points[0][1] - points[1][1]
        print(dx*dx + dy*dy)
    else:
        print(closest_pair(points))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/18221 문제
import sys
def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    grid = []
    s_pos = None
    p_pos = None
    for i in range(n):
        row = []
        for j in range(n):
            val = int(input[idx])
            idx += 1
            row.append(val)
            if val == 2:
                s_pos = (i, j)
            elif val == 5:
                p_pos = (i, j)
        grid.append(row)
    s_x, s_y = s_pos
    p_x, p_y = p_pos
    # 거리 제곱 계산
    distance_sq = (s_x - p_x)**2 + (s_y - p_y)**2
    if distance_sq < 25:
        print(0)
        return
    # 직사각형 경계 계산
    min_x = min(s_x, p_x)
    max_x = max(s_x, p_x)
    min_y = min(s_y, p_y)
    max_y = max(s_y, p_y)
    cnt = 0
    # 같은 행 또는 열 처리
    if s_x == p_x or s_y == p_y:
        if s_x == p_x:  # 같은 열
            for y in range(min_y, max_y + 1):
                if grid[s_x][y] == 1:
                    cnt += 1
        else:  # 같은 행
            for x in range(min_x, max_x + 1):
                if grid[x][s_y] == 1:
                    cnt += 1
    else:  # 직사각형 영역 처리
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if grid[x][y] == 1:
                    cnt += 1
    print(1 if cnt >= 3 else 0)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/13411 문제
import sys
input = sys.stdin.readline
n = int(input())  # 로봇의 수 입력
robots = []  # 로봇 정보를 저장할 리스트
for i in range(1, n + 1):  # 1부터 n까지 반복
    x, y, v = map(int, input().split())  # 로봇의 x좌표, y좌표, 미사일 속도 입력
    distance = (x**2 + y**2)**0.5  # 원점으로부터의 거리 계산 (피타고라스 정리)
    time = distance / v  # 미사일이 로봇에 도달하는 시간 계산
    robots.append((time, i))  # 시간과 로봇 번호를 튜플로 저장
robots.sort()  # 시간 순으로 정렬, 시간이 같으면 로봇 번호 순으로 정렬
for time, robot_number in robots:  # 정렬된 순서대로 반복
    print(robot_number)  # 로봇 번호 출력

#https://www.acmicpc.net/problem/22942 문제
import sys
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    events = []
    idx = 1
    for i in range(n):
        x = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        left = x - r
        right = x + r
        events.append((left, True, i))  # (좌표, 열림 여부, 로봇 번호)
        events.append((right, False, i))
    # x 좌표 기준 정렬 (같은 x 경우 열린 이벤트 우선)
    events.sort(key=lambda x: (x[0], not x[1]))
    marked = set()
    stack = []
    for event in events:
        x, is_open, robot_id = event
        # 중복 좌표 검증
        if x in marked:
            print("NO")
            return
        marked.add(x)
        if is_open:
            stack.append(robot_id)
        else:
            # 스택 무결성 검증
            if not stack or stack[-1] != robot_id:
                print("NO")
                return
            stack.pop()
    print("YES")
if __name__ == "__main__":
    main()
