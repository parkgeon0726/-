#4.4 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/32025 문제
H = int(input())
W = int(input())
print(min(H, W) * 50)

#https://www.acmicpc.net/problem/16483 문제
T = int(input())
result = (T / 2) ** 2
print(round(result))

#https://www.acmicpc.net/problem/20215 문제
import math
# 입력 받기
w, h = map(int, input().split())
# 결과 계산
diagonal = math.sqrt(w**2 + h**2)
rectangle = w + h
difference = rectangle - diagonal
# 출력 형식 처리
if abs(difference - round(difference)) < 1e-9:
    print(round(difference))
else:
    print(f"{difference:.9f}")

#https://www.acmicpc.net/problem/20353 문제
import math
# 입력: 아트리움의 면적
a = int(input())
# 변의 길이 계산: 면적의 제곱근
side_length = math.sqrt(a)
# 둘레 계산: 4 * 변의 길이
perimeter = 4 * side_length
# 출력: 둘레
print(perimeter)

#https://www.acmicpc.net/problem/20352 문제
import math
def calculate_fence_length(area):
    # 면적으로부터 반지름 계산
    radius = math.sqrt(area / math.pi)
    # 둘레(울타리 길이) 계산
    perimeter = 2 * math.pi * radius
    return perimeter
# 입력 받기
area = int(input())
# 울타리 길이 계산
fence_length = calculate_fence_length(area)
# 결과 출력
print(fence_length)
