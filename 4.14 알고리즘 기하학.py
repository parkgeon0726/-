#4.14 알고리즘 기하학 관련3문제

#https://www.acmicpc.net/problem/6439 문제
def ccw(x1, y1, x2, y2, x3, y3):
    """세 점의 방향성을 판단하는 함수 (Counter-Clockwise)"""
    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if result > 0:  # 반시계 방향
        return 1
    elif result < 0:  # 시계 방향
        return -1
    else:  # 일직선
        return 0
def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    """두 선분이 교차하는지 확인하는 함수"""
    # CCW 값 계산
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    # 교차 여부 판단
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        # 선분이 일직선인 경우, 겹치는지 확인
        if ccw1 == 0 and ccw2 == 0:
            # 선분의 투영된 범위가 겹치는지 확인
            if max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4)) and \
               max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4)):
                return True
            return False
        return True
    return False
def is_inside_rectangle(x, y, x_min, y_min, x_max, y_max):
    """점이 직사각형 내부에 있는지 확인하는 함수"""
    return x_min <= x <= x_max and y_min <= y <= y_max
def is_segment_rectangle_intersect(x_start, y_start, x_end, y_end, x_left, y_top, x_right, y_bottom):
    """선분과 직사각형이 교차하는지 확인하는 함수"""
    # 직사각형 좌표 정규화
    x_min = min(x_left, x_right)
    x_max = max(x_left, x_right)
    y_min = min(y_top, y_bottom)
    y_max = max(y_top, y_bottom)
    # 선분의 끝점이 직사각형 내부에 있는지 확인
    if is_inside_rectangle(x_start, y_start, x_min, y_min, x_max, y_max) or \
       is_inside_rectangle(x_end, y_end, x_min, y_min, x_max, y_max):
        return True
    # 선분과 직사각형의 네 변이 교차하는지 확인
    # 위쪽 변: (x_min, y_max) to (x_max, y_max)
    if is_cross(x_start, y_start, x_end, y_end, x_min, y_max, x_max, y_max):
        return True
    # 오른쪽 변: (x_max, y_max) to (x_max, y_min)
    if is_cross(x_start, y_start, x_end, y_end, x_max, y_max, x_max, y_min):
        return True
    # 아래쪽 변: (x_min, y_min) to (x_max, y_min)
    if is_cross(x_start, y_start, x_end, y_end, x_min, y_min, x_max, y_min):
        return True
    # 왼쪽 변: (x_min, y_max) to (x_min, y_min)
    if is_cross(x_start, y_start, x_end, y_end, x_min, y_max, x_min, y_min):
        return True
    return False
def main():
    t = int(input())
    for _ in range(t):
        x_start, y_start, x_end, y_end, x_left, y_top, x_right, y_bottom = map(int, input().split())
        if is_segment_rectangle_intersect(x_start, y_start, x_end, y_end, x_left, y_top, x_right, y_bottom):
            print("T")
        else:
            print("F")
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/15803 문제
# 세 점의 좌표를 입력받기
points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))
# 세 점 A(x1,y1), B(x2,y2), C(x3,y3)에 대해
x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]
# CCW 알고리즘 적용
ccw = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
if ccw == 0:  # 세 점이 일직선 상에 있는 경우
    print("WHERE IS MY CHICKEN?")
else:  # 세 점이 일직선 상에 있지 않은 경우
    print("WINNER WINNER CHICKEN DINNER!")

#https://www.acmicpc.net/problem/26566 문제
import math
n = int(input())  # 데이터셋 개수
for _ in range(n):
    A1, P1 = map(int, input().split())  # 피자 조각의 면적과 가격
    R1, P2 = map(int, input().split())  # 전체 피자의 반지름과 가격
    # 단위 가격당 피자 면적 계산
    slice_value = A1 / P1  # 피자 조각의 가성비
    whole_value = (math.pi * R1 * R1) / P2  # 전체 피자의 가성비
    # 더 경제적인 옵션 선택
    if slice_value > whole_value:
        print("Slice of pizza")
    else:
        print("Whole pizza")
