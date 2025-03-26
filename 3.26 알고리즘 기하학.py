#3.26 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/10101 문제
#angle1 = int(input())
#angle2 = int(input())
#angle3 = int(input())
#angle_sum = angle1 + angle2 + angle3
#if angle_sum != 180:
#    print("Error")  # 세 각의 합이 180이 아니면 Error
#elif angle1 == 60 and angle2 == 60 and angle3 == 60:
#    print("Equilateral")  # 세 각이 모두 60이면 Equilateral
#elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
#    print("Isosceles")  # 두 각이 같으면 Isosceles
#else:
#    print("Scalene")  # 같은 각이 없으면 Scalene

#https://www.acmicpc.net/problem/27323 문제
# 세로 길이와 가로 길이를 입력받습니다.
#A = int(input())
#B = int(input())
# 제한 조건 확인
#if 1 <= A <= 100 and 1 <= B <= 100:
    # 직사각형의 넓이를 계산하여 출력합니다.
#    print(A * B)

#https://www.acmicpc.net/problem/5073 문제
#def triangle_type(a, b, c):
    # 세 변의 길이를 정렬하여 가장 긴 변이 마지막에 오도록 설정
#    sides = sorted([a, b, c])
    # 삼각형의 조건 확인 (가장 긴 변의 길이가 나머지 두 변의 합보다 크거나 같으면 Invalid)
#    if sides[0] + sides[1] <= sides[2]:
#        return "Invalid"
    # 삼각형의 종류 판별
#    if sides[0] == sides[1] == sides[2]:
#        return "Equilateral"
#    elif sides[0] == sides[1] or sides[1] == sides[2]:
#        return "Isosceles"
#    else:
#        return "Scalene"
# 입력을 처리하고 결과를 출력하는 함수
#def process_triangle_inputs():
#    while True:
        # 사용자 입력 받기
#        user_input = input()
        # 입력된 값을 정수로 변환
#        a, b, c = map(int, user_input.split())
        # 종료 조건 확인
#        if a == 0 and b == 0 and c == 0:
#            break
        # 결과 출력
#        print(triangle_type(a, b, c))
# 함수 실행
#process_triangle_inputs()

#https://www.acmicpc.net/problem/3053 문제
#import math
#def calculate_areas(radius):
    # 유클리드 기하학에서 원의 넓이 계산
#    euclidean_area = math.pi * radius ** 2
    # 택시 기하학에서 원의 넓이 계산
#    taxi_area = 2 * radius ** 2
    # 결과 출력 (소수점 6자리까지)
#    print(f"{euclidean_area:.6f}")
#    print(f"{taxi_area:.6f}")
# 반지름 입력 받기
#radius = int(input())
#calculate_areas(radius)

#https://www.acmicpc.net/problem/9063 문제
# 입력: 점의 개수와 각 점의 좌표
#N = int(input())  # 점의 개수 입력
#points = [tuple(map(int, input().split())) for _ in range(N)]  # 각 점의 좌표 입력
# 직사각형의 경계 계산
#min_x = min(point[0] for point in points)
#max_x = max(point[0] for point in points)
#min_y = min(point[1] for point in points)
#max_y = max(point[1] for point in points)
# 직사각형 넓이 계산
#area = (max_x - min_x) * (max_y - min_y)
# 결과 출력
#print(area)