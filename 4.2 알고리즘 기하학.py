#4.2 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/16600 문제
import math
# 면적을 입력받음
area = int(input())
# 정사각형의 한 변의 길이 계산 (면적의 제곱근)
side_length = math.sqrt(area)
# 둘레 계산 (한 변의 길이 × 4)
perimeter = 4 * side_length
# 결과 출력 (오차 범위를 고려한 정밀도)
print(perimeter)

#https://www.acmicpc.net/problem/9366 문제
T = int(input())  # 테스트 케이스의 개수
for i in range(1, T + 1):
    # 세 변의 길이 입력
    sides = list(map(int, input().split()))
    # 오름차순 정렬
    sides.sort()
    # 삼각형 성립 조건 확인
    if sides[0] + sides[1] <= sides[2]:
        print(f"Case #{i}: invalid!")
    else:
        # 삼각형 타입 판별
        if sides[0] == sides[1] == sides[2]:  # 정삼각형
            print(f"Case #{i}: equilateral")
        elif sides[0] == sides[1] or sides[1] == sides[2]:  # 이등변삼각형
            print(f"Case #{i}: isosceles")
        else:  # 부등변삼각형
            print(f"Case #{i}: scalene")

#https://www.acmicpc.net/problem/22938 문제
# 두 과녁이 완전히 동일한 경우 처리
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
# 동일한 원인 경우 예외 처리
if x1 == x2 and y1 == y2 and r1 == r2:
    print("YES")
else:
    # 중심 거리 제곱 계산
    dx = x2 - x1
    dy = y2 - y1
    d_sq = dx*dx + dy*dy
    # 반지름 연산
    sum_r_sq = (r1 + r2)**2
    diff_r_sq = (abs(r1 - r2))**2
    # 두 원이 겹치는 조건 체크 (한 점 접촉 제외)
    if diff_r_sq < d_sq < sum_r_sq:
        print("YES")
    else:
        print("NO")

#https://www.acmicpc.net/problem/16693 문제
import math
# 피자 조각 정보 입력
A1, P1 = map(int, input().split())
# 원형 피자 정보 입력
R1, P2 = map(int, input().split())
# 단위 가격당 면적 계산
조각_가성비 = A1 / P1
원형_면적 = math.pi * R1 ** 2
원형_가성비 = 원형_면적 / P2
# 결과 비교
print("Whole pizza" if 원형_가성비 > 조각_가성비 else "Slice of pizza")

#https://www.acmicpc.net/problem/10655 문제
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
# 체크포인트 수 입력
n = int(input())
# 체크포인트 좌표 입력
checkpoints = []
for _ in range(n):
    x, y = map(int, input().split())
    checkpoints.append((x, y))
# 모든 체크포인트를 방문할 때의 총 거리 계산
total_distance = 0
for i in range(1, n):
    total_distance += manhattan_distance(checkpoints[i-1], checkpoints[i])
# 각 체크포인트를 건너뛸 때의 최소 거리 계산
min_distance = float('inf')  # 충분히 큰 값으로 초기화
for i in range(1, n-1):
    # i번째 체크포인트를 건너뛸 때의 거리
    skip_distance = total_distance
    # i-1에서 i, i에서 i+1로 가는 거리를 빼고
    skip_distance -= manhattan_distance(checkpoints[i-1], checkpoints[i])
    skip_distance -= manhattan_distance(checkpoints[i], checkpoints[i+1])
    # i-1에서 i+1로 직접 가는 거리를 더함
    skip_distance += manhattan_distance(checkpoints[i-1], checkpoints[i+1])
    min_distance = min(min_distance, skip_distance)
print(min_distance)