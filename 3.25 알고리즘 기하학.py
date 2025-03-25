#3.25 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/14681 문제
# x와 y 좌표를 입력받습니다.
#x = int(input())
#y = int(input())
# 조건에 따라 사분면 번호를 출력합니다.
#if x > 0 and y > 0:
#    print(1)  # 제1사분면
#elif x < 0 and y > 0:
#    print(2)  # 제2사분면
#elif x < 0 and y < 0:
#    print(3)  # 제3사분면
#elif x > 0 and y < 0:
#    print(4)  # 제4사분면

#https://www.acmicpc.net/problem/1085 문제
# 입력값 받기
#x, y, w, h = map(int, input().split())
# 각 변까지의 거리 계산
#distance_to_left = x
#distance_to_right = w - x
#distance_to_bottom = y
#distance_to_top = h - y
# 최솟값 계산
#min_distance = min(distance_to_left, distance_to_right, distance_to_bottom, distance_to_top)
# 결과 출력
#print(min_distance)

#https://www.acmicpc.net/problem/4153 문제
# 직각삼각형 여부를 확인하는 함수
#def is_right_triangle(a, b, c):
#    sides = sorted([a, b, c])  # 세 변의 길이를 정렬하여 가장 긴 변을 빗변으로 설정
#    return sides[0]**2 + sides[1]**2 == sides[2]**2
# 입력 처리 및 결과 출력
#while True:
    # 사용자 입력 받기
#    a, b, c = map(int, input().split())
    
    # 종료 조건
#    if a == 0 and b == 0 and c == 0:
#        break
    
    # 직각삼각형 여부 확인
#    if is_right_triangle(a, b, c):
#        print("right")
#    else:
#        print("wrong")

#https://www.acmicpc.net/problem/3009 문제
# 입력받기
#x_coords = []
#y_coords = []
#for _ in range(3):
#    x, y = map(int, input().split())
#    x_coords.append(x)
#    y_coords.append(y)
# 네 번째 점의 x 좌표 찾기
#if x_coords.count(x_coords[0]) == 1:
#    fourth_x = x_coords[0]
#elif x_coords.count(x_coords[1]) == 1:
#    fourth_x = x_coords[1]
#else:
#    fourth_x = x_coords[2]
# 네 번째 점의 y 좌표 찾기
#if y_coords.count(y_coords[0]) == 1:
#    fourth_y = y_coords[0]
#elif y_coords.count(y_coords[1]) == 1:
#    fourth_y = y_coords[1]
#else:
#    fourth_y = y_coords[2]
# 결과 출력
#print(fourth_x, fourth_y)

#https://www.acmicpc.net/problem/1002 문제
#import math
#def calculate_positions(test_cases):
#    results = []
#    for case in test_cases:
#        x1, y1, r1, x2, y2, r2 = case        
        # 두 원의 중심 사이 거리 계산
#        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)        
        # 교점 개수 판별
#        if distance == 0 and r1 == r2:
#            results.append(-1)  # 두 원이 완전히 겹침 (무한대의 교점)
#        elif distance > r1 + r2: 
#            results.append(0)  # 두 원이 서로 떨어져 있음 (교점 없음)
#        elif distance < abs(r1 - r2): 
#            results.append(0)  # 한 원이 다른 원 내부에 있음 (교점 없음)
#        elif distance == r1 + r2 or distance == abs(r1 - r2): 
#            results.append(1)  # 두 원이 외접하거나 내접 (교점 하나)
#        else:
#            results.append(2)  # 두 원이 교차함 (교점 두 개)
#    return results
# 입력 처리
#T = int(input())  # 테스트 케이스 개수
#cases = [tuple(map(int, input().split())) for _ in range(T)]
# 결과 계산 및 출력
#output = calculate_positions(cases)
#for result in output:
#    print(result)