#4.1 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/1069 문제
import math
def solution():
    X, Y, D, T = map(int, input().split())
    # 원점까지의 직선 거리 계산
    dist = math.sqrt(X**2 + Y**2)
    # 걷기만 하는 것이 빠른 경우
    if dist <= T or T >= D:
        return dist
    # 점프만 하는 것이 빠른 경우 (직선 거리가 D의 배수인 경우)
    if dist % D == 0:
        return (dist // D) * T
    # 세 가지 전략 비교
    # 1. 점프로 일직선 상에서 최대한 진행 후 남은 거리 걸어서 가기
    j1 = dist // D
    w1 = dist - j1 * D
    time1 = j1 * T + w1
    # 2. 점프를 한 번 더 하고 넘치는 거리 걸어서 돌아오기
    j2 = dist // D + 1
    w2 = j2 * D - dist
    time2 = j2 * T + w2
    # 3. 이등변 삼각형 형태로 점프만 사용
    j3 = dist // D + 1 if dist > D else 2
    time3 = j3 * T
    return min(time1, time2, time3)
if __name__ == '__main__':
    print(solution())

#https://www.acmicpc.net/problem/2022 문제
import math
def calculate_width(x, y, c):
    # 이진 탐색을 위한 초기 범위 설정
    left, right = 0, min(x, y)
    # 수렴 조건을 1e-6으로 설정 (충분한 정밀도)
    while right - left > 1e-6:
        mid = (left + right) / 2
        # 사다리 높이 계산
        h1 = math.sqrt(x*x - mid*mid)
        h2 = math.sqrt(y*y - mid*mid)
        # 교차점 높이 계산
        current_c = (h1 * h2) / (h1 + h2)
        # 이진 탐색 조건
        if current_c > c:
            left = mid
        else:
            right = mid
    return left
# 입력 처리
x, y, c = map(float, input().split())
# 결과 출력
print(f"{calculate_width(x, y, c):.3f}")

#https://www.acmicpc.net/problem/6322 문제
import math
def solve_right_triangle():
    case = 1
    first_case = True  # 첫 번째 케이스 여부 확인 플래그
    while True:
        a, b, c = map(int, input().split())
        # 종료 조건
        if a == 0 and b == 0 and c == 0:
            break
        # 테스트 케이스 간 빈 줄 처리
        if not first_case:
            print()
        first_case = False
        print(f"Triangle #{case}")
        # 변수 계산 로직
        if a == -1:
            if c > b and c**2 - b**2 > 0:
                result = math.sqrt(c**2 - b**2)
                print(f"a = {result:.3f}")
            else:
                print("Impossible.")
        elif b == -1:
            if c > a and c**2 - a**2 > 0:
                result = math.sqrt(c**2 - a**2)
                print(f"b = {result:.3f}")
            else:
                print("Impossible.")
        elif c == -1:
            result = math.sqrt(a**2 + b**2)
            print(f"c = {result:.3f}")
        case += 1
if __name__ == "__main__":
    solve_right_triangle()

#https://www.acmicpc.net/problem/6502 문제
import math
def check_pizza_fit():
    case = 1
    while True:
        # 입력 처리
        input_data = input().strip()
        if input_data == '0':
            break
        # 데이터 분할 및 변환
        r, w, l = map(int, input_data.split())
        # 식탁 지름 계산
        table_diameter = 2 * r
        # 피자 대각선 길이 계산
        pizza_diagonal = math.sqrt(w**2 + l**2)
        # 조건 검증 및 결과 출력
        if table_diameter >= pizza_diagonal:
            print(f"Pizza {case} fits on the table.")
        else:
            print(f"Pizza {case} does not fit on the table.")
        case += 1
if __name__ == "__main__":
    check_pizza_fit()

#https://www.acmicpc.net/problem/20149 문제
def ccw(a, b, c):
    res = (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])
    return 1 if res > 0 else (-1 if res < 0 else 0)
def is_overlap(a1, a2, b1, b2):
    return max(a1, a2) >= min(b1, b2) and max(b1, b2) >= min(a1, a2)
def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    A, B, C, D = (x1,y1), (x2,y2), (x3,y3), (x4,y4)
    # CCW 계산
    abc = ccw(A, B, C)
    abd = ccw(A, B, D)
    cda = ccw(C, D, A)
    cdb = ccw(C, D, B)
    cross = False
    # 모든 CCW가 0이면 일직선
    is_colinear = (abc == 0 and abd == 0 and cda == 0 and cdb == 0)
    if is_colinear:
        # x, y 축 투영 검사
        x_overlap = is_overlap(x1, x2, x3, x4)
        y_overlap = is_overlap(y1, y2, y3, y4)
        cross = x_overlap and y_overlap
    else:
        cross = (abc * abd <= 0) and (cda * cdb <= 0)
    if not cross:
        print(0)
        return
    print(1)
    # 교차점 처리
    points = set()
    # 일직선인 경우 공통 끝점 검출
    if is_colinear:
        for p in [A, B]:
            if (min(x3, x4) <= p[0] <= max(x3, x4)) and (min(y3, y4) <= p[1] <= max(y3, y4)):
                points.add(p)
        for p in [C, D]:
            if (min(x1, x2) <= p[0] <= max(x1, x2)) and (min(y1, y2) <= p[1] <= max(y1, y2)):
                points.add(p)
        if len(points) == 1:
            x, y = points.pop()
            print(f"{x:.9f} {y:.9f}")
        return
    # 일반 교차점 계산
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if denom == 0: return
    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
    s = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if 0 <= t <= 1 and 0 <= s <= 1:
        px = x1 + t*(x2-x1)
        py = y1 + t*(y2-y1)
        print(f"{px:.9f} {py:.9f}")
solve()
