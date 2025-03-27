#3.27 알고리즘 기하학 관련10문제

#https://www.acmicpc.net/problem/1004 문제
#def count_entries_exits(test_cases):
#    results = []
#    for case in test_cases:
#        x1, y1, x2, y2 = case["start"]
#        planets = case["planets"]
#        count = 0
#        for cx, cy, r in planets:
            # 출발점이 행성계 내부에 있는지 확인
#            start_inside = (x1 - cx)**2 + (y1 - cy)**2 < r**2
            # 도착점이 행성계 내부에 있는지 확인
#            end_inside = (x2 - cx)**2 + (y2 - cy)**2 < r**2
            # 한 점은 내부에 있고 다른 점은 외부에 있을 경우 진입/이탈 횟수 증가
#            if start_inside != end_inside:
#                count += 1
#        results.append(count)
#    return results
# 입력 처리 함수
#def parse_input():
#    T = int(input())  # 테스트 케이스 개수
#    test_cases = []
#    for _ in range(T):
#        x1, y1, x2, y2 = map(int, input().split())  # 출발점과 도착점 좌표
#        n = int(input())  # 행성계 개수
#        planets = []
#        for _ in range(n):
#            cx, cy, r = map(int, input().split())  # 행성계 정보 (중심 좌표와 반지름)
#            planets.append((cx, cy, r))
#        test_cases.append({"start": (x1, y1, x2, y2), "planets": planets})
#    return test_cases
# 실행 부분
#if __name__ == "__main__":
#    test_cases = parse_input()
#    results = count_entries_exits(test_cases)
#    for result in results:
#        print(result)

#https://www.acmicpc.net/problem/14215 문제
#def max_triangle_perimeter(a, b, c):
    # 막대 길이를 내림차순으로 정렬
#    sticks = sorted([a, b, c], reverse=True)
    # 삼각형 조건을 만족하는지 확인
#    while sticks[0] >= sticks[1] + sticks[2]:
        # 가장 긴 막대의 길이를 줄여나감
#        sticks[0] -= 1
#        sticks = sorted(sticks, reverse=True)
    # 조건을 만족하면 둘레 반환
#    return sum(sticks)
# 예제 입력
#a, b, c = map(int, input().split())
#print(max_triangle_perimeter(a, b, c))

#https://www.acmicpc.net/problem/2166 문제
#def polygon_area(points):
#    n = len(points)
#    area = 0
    # 신발끈 공식 적용
#    for i in range(n):
#        x1, y1 = points[i]
#        x2, y2 = points[(i + 1) % n]  # 다음 점 (마지막 점의 경우 첫 점으로 돌아감)
#        area += x1 * y2 - x2 * y1
    # 면적 계산 및 절대값 처리
#    return round(abs(area) / 2, 1)
# 입력 처리
#n = int(input())
#points = [tuple(map(int, input().split())) for _ in range(n)]
# 결과 출력
#print(polygon_area(points))

#https://www.acmicpc.net/problem/2477 문제
#def calculate_melon_count(k, directions):
    # 방향과 길이를 분리하여 저장
#    lengths = [length for _, length in directions]
    # 가장 긴 변과 두 번째로 긴 변 찾기
#    max_length = 0
#    max_index = 0
#    for i in range(6):
#        if lengths[i] * lengths[(i + 1) % 6] > max_length:
#            max_length = lengths[i] * lengths[(i + 1) % 6]
#            max_index = i
    # 큰 직사각형의 면적
#    total_area = max_length
    # 작은 직사각형의 면적
#    small_area = lengths[(max_index + 3) % 6] * lengths[(max_index + 4) % 6]
    # 실제 밭의 면적
#    field_area = total_area - small_area
    # 참외 개수 계산
#    melon_count = field_area * k
#    return melon_count
# 입력 처리
#k = int(input())  # 1m²당 자라는 참외 개수
#directions = [tuple(map(int, input().split())) for _ in range(6)]  # 방향과 길이 입력
# 결과 출력
#print(calculate_melon_count(k, directions))

#https://www.acmicpc.net/problem/11758 문제
#def find_direction(x1, y1, x2, y2, x3, y3):
    # 벡터 P1P2와 P2P3의 외적 계산
#    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    # 방향 판별
#    if cross_product > 0:
#        return 1  # 반시계 방향
#    elif cross_product < 0:
#        return -1  # 시계 방향
#    else:
#        return 0  # 일직선
# 입력 받기
#x1, y1 = map(int, input().split())
#x2, y2 = map(int, input().split())
#x3, y3 = map(int, input().split())
# 결과 출력
#print(find_direction(x1, y1, x2, y2, x3, y3))

#https://www.acmicpc.net/problem/1297 문제
#import math
#def calculate_tv_dimensions(diagonal, height_ratio, width_ratio):
    # 스케일링 팩터 계산
#    scaling_factor = diagonal / math.sqrt(height_ratio**2 + width_ratio**2)
    # 실제 높이와 너비 계산
#    actual_height = math.floor(scaling_factor * height_ratio)
#    actual_width = math.floor(scaling_factor * width_ratio)
#    return actual_height, actual_width
# 입력 받기
#D, H, W = map(int, input().split())
# 실제 높이와 너비 계산
#height, width = calculate_tv_dimensions(D, H, W)
# 결과 출력
#print(height, width)

#https://www.acmicpc.net/problem/10569 문제
# 볼록다면체의 면의 수를 계산하는 함수
#def calculate_faces(test_cases):
#    results = []
#    for V, E in test_cases:
#        F = 2 + E - V  # 오일러의 공식: V - E + F = 2
#        results.append(F)
#    return results
# 입력 처리
#T = int(input())  # 테스트 케이스 수
#test_cases = []
#for _ in range(T):
#    V, E = map(int, input().split())
#    test_cases.append((V, E))
# 각 테스트 케이스에 대해 면의 수 계산
#faces = calculate_faces(test_cases)
# 결과 출력
#for face_count in faces:
#    print(face_count)

#https://www.acmicpc.net/problem/16486 문제
# 운동장의 한 바퀴 둘레를 계산하는 프로그램
#def calculate_perimeter(d1, d2):
    # 원주율 값 설정
#    pi = 3.141592
    # 운동장 둘레 계산: 직사각형의 가로 길이 + 두 반원의 둘레
#    perimeter = 2 * d1 + 2 * pi * d2
#    return perimeter
# 입력값 받기
#d1 = int(input())  # 직사각형의 가로 길이
#d2 = int(input())  # 반원의 반지름 길이
# 결과 출력
#result = calculate_perimeter(d1, d2)
#print(f"{result:.6f}")

#https://www.acmicpc.net/problem/3034 문제
#import math
# 입력값 받기
#N, W, H = map(int, input().split())
#match_lengths = [int(input()) for _ in range(N)]
# 박스의 대각선 길이 계산
#diagonal = math.sqrt(W**2 + H**2)
# 성냥이 박스에 들어갈 수 있는지 확인
#for length in match_lengths:
#    if length <= diagonal:
#        print("DA")
#    else:
#        print("NE")

#https://www.acmicpc.net/problem/1027 문제
#import math
# 입력 처리
#N = int(input())
#heights = list(map(int, input().split()))
#def can_see(a, b, heights):
#    """빌딩 a에서 b를 볼 수 있는지 확인"""
#    x1, y1 = a, heights[a]
#    x2, y2 = b, heights[b]
#    for i in range(a + 1, b):
        # 두 빌딩을 잇는 직선의 기울기와 y절편 계산
#        slope = (y2 - y1) / (x2 - x1)
#        intercept = y1 - slope * x1
        # i번째 빌딩이 직선 위에 있는지 확인
#        if heights[i] >= slope * i + intercept:
#            return False
#    return True
# 각 빌딩에서 보이는 빌딩 수 계산
#max_visible = 0
#for i in range(N):
#    visible_count = 0
    # 왼쪽 방향으로 볼 수 있는 빌딩 확인
#    for j in range(i - 1, -1, -1):
#        if can_see(j, i, heights):
#            visible_count += 1
    # 오른쪽 방향으로 볼 수 있는 빌딩 확인
#    for j in range(i + 1, N):
#        if can_see(i, j, heights):
#            visible_count += 1
    # 최대값 갱신
#    max_visible = max(max_visible, visible_count)
# 결과 출력
#print(max_visible)