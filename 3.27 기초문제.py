#3.27 조건과 반복 관련문제풀이 (새싹문제풀이임)

#https://www.acmicpc.net/problem/1330 문제
#답: A, B = map(int, input().split())
#답: if A > B:
#답:     print('>')
#답: elif A < B:
#답:     print('<')
#답: else:
#답:     print('==')

#https://www.acmicpc.net/problem/9498 문제
#답: score = int(input())
#답: if 90 <= score <= 100:
#답:     print('A')
#답: elif 80 <= score <= 89:
#답:     print('B')
#답: elif 70 <= score <= 79:
#답:     print('C')
#답: elif 60 <= score <= 69:
#답:     print('D')
#답: else:
#답:     print('F')

#https://www.acmicpc.net/problem/2753 문제
#답: year = int(input())
#답: if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#답:     print(1)
#답: else:
#답:     print(0)

#https://www.acmicpc.net/problem/2420 문제
#N, M = map(int, input().split())
# 두 유명도의 차이를 계산합니다.
#difference = abs(N - M)
#print(difference)

#https://www.acmicpc.net/problem/2741 문제
#N = int(input())
# 1부터 N까지 한 줄씩 출력합니다.
#for i in range(1, N + 1):
#    print(i)

#https://www.acmicpc.net/problem/10872 문제
#N = int(input())
# 팩토리얼 계산을 위한 변수 초기화
#factorial = 1
# 1부터 N까지 곱하여 팩토리얼 계산
#for i in range(1, N + 1):
#    factorial *= i
#print(factorial)

#https://www.acmicpc.net/problem/10950 문제
#T = int(input())
# T번 반복하여 각 테스트 케이스를 처리합니다.
#for _ in range(T):
    # A와 B를 입력받아 더한 결과를 출력합니다.
#    A, B = map(int, input().split())
#    print(A + B)

#https://www.acmicpc.net/problem/10952 문제
#while True:
    # A와 B를 입력받습니다.
#    A, B = map(int, input().split())
    # 입력의 마지막인 "0 0"이 들어오면 종료합니다.
#    if A == 0 and B == 0:
#        break
    # A와 B의 합을 출력합니다.
#    print(A + B)

#https://www.acmicpc.net/problem/2739 문제
#N = int(input())
# 1부터 9까지 반복하여 구구단 출력
#for i in range(1, 10):
#    print(f"{N} * {i} = {N * i}")

#https://www.acmicpc.net/problem/2438 문제
#N = int(input())
# 1부터 N까지 반복하여 별을 출력합니다.
#for i in range(1, N + 1):
#    print('*' * i)

#https://www.acmicpc.net/problem/10951 문제
#import sys
# 입력을 여러 줄로 받기 위해 sys.stdin을 사용
#for line in sys.stdin:
#    try:
        # 각 줄에서 A와 B를 읽어오기
#        A, B = map(int, line.split())
        # 조건에 맞는 경우 출력
#        if 0 < A < 10 and 0 < B < 10:
#            print(A + B)
#    except ValueError:
        # 입력이 잘못된 경우 무시하고 계속 진행
#        continue