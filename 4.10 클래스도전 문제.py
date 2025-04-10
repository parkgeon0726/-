# 4.10 클래스 도전 5문제

#https://www.acmicpc.net/problem/9095 문제
import sys
# 테스트 케이스의 개수
T = int(input())
# dp 배열 초기화 (문제에서 n은 11보다 작다고 했으므로 크기를 11로 설정)
dp = [0] * 11
dp[1] = 1  # 1을 만드는 방법의 수
dp[2] = 2  # 2를 만드는 방법의 수 (1+1, 2)
dp[3] = 4  # 3을 만드는 방법의 수 (1+1+1, 1+2, 2+1, 3)
# 점화식을 이용하여 dp 배열 채우기
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# 각 테스트 케이스에 대해 결과 출력
for _ in range(T):
    n = int(input())
    print(dp[n])

#https://www.acmicpc.net/problem/9375 문제
T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print(0)
        continue
    clothes = {}
    for _ in range(n):
        _, category = input().split()
        clothes[category] = clothes.get(category, 0) + 1
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    print(result - 1)

#https://www.acmicpc.net/problem/9461 문제
# 테스트 케이스의 개수를 입력받음
T = int(input())
# 파도반 수열을 계산하기 위한 리스트 초기화
padovan = [0] * 101
padovan[1] = padovan[2] = padovan[3] = 1
# 파도반 수열 계산 (점화식: P(n) = P(n-2) + P(n-3), n ≥ 4)
for i in range(4, 101):
    padovan[i] = padovan[i-2] + padovan[i-3]
# 각 테스트 케이스에 대해 결과 출력
for _ in range(T):
    N = int(input())
    print(padovan[N])

#https://www.acmicpc.net/problem/11659 문제
import sys
# 입력 받기
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
# 누적 합 배열 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]
# 쿼리 처리
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    # i부터 j까지의 합 계산
    result = prefix_sum[j] - prefix_sum[i - 1]
    print(result)

#https://www.acmicpc.net/problem/11726 문제
import sys
# 입력 받기
n = int(sys.stdin.readline())
# 작은 케이스 처리
if n <= 2:
    print(n)
else:
    # DP 배열 초기화
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    # 점화식을 이용한 DP 배열 채우기
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    print(dp[n])
