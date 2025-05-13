#5.13 클래스도전 관련5문제

#https://www.acmicpc.net/problem/11053 문제
# 백준 11053번 가장 긴 증가하는 부분 수열
# 수열의 크기 입력
n = int(input())
# 수열 입력
array = list(map(int, input().split()))
# dp 테이블 초기화 (기본값 1)
dp = [1] * n
# 모든 원소에 대해 가장 긴 증가하는 부분 수열 계산
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:  # 현재 원소가 이전 원소보다 큰 경우
            dp[i] = max(dp[i], dp[j] + 1)  # dp 테이블 갱신
# 가장 긴 증가하는 부분 수열의 길이 출력
print(max(dp))

#https://www.acmicpc.net/problem/11725 문제
import sys
from collections import deque
# 노드 개수 입력
n = int(sys.stdin.readline())
# 인접 리스트 초기화
adj = [[] for _ in range(n + 1)]
# 간선 정보 입력 및 인접 리스트 구성
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
# 부모 노드 저장 배열
parent = [0] * (n + 1)
visited = [False] * (n + 1)
# BFS 초기 설정
q = deque()
q.append(1)
visited[1] = True
# BFS 수행
while q:
    current = q.popleft()
    for neighbor in adj[current]:
        if not visited[neighbor]:
            parent[neighbor] = current  # 부모 노드 기록[1][2][4]
            visited[neighbor] = True    # 방문 처리[3][5]
            q.append(neighbor)          # 다음 탐색 노드 추가[6][7]
# 결과 출력
for i in range(2, n + 1):
    print(parent[i])

#https://www.acmicpc.net/problem/16953 문제
a, b = map(int, input().split())
count = 0
while b > a:
    if b % 10 == 1:  # 마지막 자리가 1인 경우
        b = b // 10
        count += 1
    elif b % 2 == 0:  # 짝수인 경우
        b = b // 2
        count += 1
    else:  # 더 이상 연산 불가
        break
print(count + 1 if b == a else -1)

#https://www.acmicpc.net/problem/1149 문제
import sys
input = sys.stdin.readline
# 집의 수 입력
n = int(input())
# 각 집을 칠하는 비용 입력
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
# DP 배열 초기화
dp = [[0, 0, 0] for _ in range(n)]
dp[0][0] = cost[0][0]  # 첫 집을 빨강으로 칠하는 비용
dp[0][1] = cost[0][1]  # 첫 집을 초록으로 칠하는 비용
dp[0][2] = cost[0][2]  # 첫 집을 파랑으로 칠하는 비용
# DP 진행
for i in range(1, n):
    # i번째 집을 빨강으로 칠하는 경우: i-1번째 집은 초록 또는 파랑이어야 함
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    # i번째 집을 초록으로 칠하는 경우: i-1번째 집은 빨강 또는 파랑이어야 함
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    # i번째 집을 파랑으로 칠하는 경우: i-1번째 집은 빨강 또는 초록이어야 함
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
# 마지막 집까지 칠했을 때의 최소 비용
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

#https://www.acmicpc.net/problem/1629 문제
def power_mod(a, b, c):
    result = 1
    a = a % c  # 초기 a를 c로 나눈 나머지로 설정
    while b > 0:
        if b % 2 == 1:  # 지수가 홀수인 경우
            result = (result * a) % c
        a = (a * a) % c  # a 제곱 후 모듈러 연산
        b = b // 2  # 지수 절반으로 감소
    return result
# 입력 받기
a, b, c = map(int, input().split())
# 결과 출력
print(power_mod(a, b, c))
