#4.9 클래스도전 5문제

#https://www.acmicpc.net/problem/17219문제
import sys
# 입력이 많으므로 sys.stdin.readline을 사용하여 입력 속도 향상
input = sys.stdin.readline
# N, M 입력 받기
N, M = map(int, input().split())
# 사이트 주소와 비밀번호 저장할 딕셔너리 생성
password_dict = {}
# N개의 사이트 주소와 비밀번호 입력 받기
for _ in range(N):
    site, password = input().split()
    password_dict[site] = password
# M개의 사이트 주소에 대한 비밀번호 찾기
for _ in range(M):
    site = input().rstrip()  # 개행 문자(\n) 제거
    print(password_dict[site])

#https://www.acmicpc.net/problem/1003 문제
# 0과 1의 호출 횟수를 저장할 배열 초기화
zeros = [0] * 41
ones = [0] * 41
# 기본값 설정
zeros[0] = 1
ones[1] = 1
# 동적 프로그래밍을 통한 사전 계산
for i in range(2, 41):
    zeros[i] = zeros[i-1] + zeros[i-2]
    ones[i] = ones[i-1] + ones[i-2]
# 테스트 케이스 처리
T = int(input())
for _ in range(T):
    N = int(input())
    print(zeros[N], ones[N])

#https://www.acmicpc.net/problem/1463 문제
def min_operations_bottom_up(n):
    # dp[i]: i를 1로 만드는 데 필요한 최소 연산 횟수
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        # 1을 빼는 연산을 기본으로 설정
        dp[i] = dp[i - 1] + 1
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1) 
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    return dp[n]
# 입력 받기
n = int(input())
print(min_operations_bottom_up(n))

#https://www.acmicpc.net/problem/2579 문제
def solve_stair_climbing(n, stairs):
    # 계단이 1개인 경우는 바로 결과 반환
    if n == 1:
        return stairs[1]
    # dp[i]: i번째 계단까지의 최대 점수
    dp = [0] * (n + 1)
    # 초기값 설정
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    # 3번째 계단부터 DP 진행
    for i in range(3, n + 1):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    return dp[n]
# 입력 받기
n = int(input())
stairs = [0] * (n + 1)  # 1-indexed 배열 사용
for i in range(1, n + 1):
    stairs[i] = int(input())
# 결과 출력
print(solve_stair_climbing(n, stairs))

#https://www.acmicpc.net/problem/2606 문제
# DFS 방식
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    for i in graph[v]:  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)
# 입력 받기
n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 컴퓨터 쌍의 수
# 그래프 초기화
graph = [[] for _ in range(n + 1)]
# 그래프 구성하기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프
# 방문 여부를 체크할 리스트
visited = [False] * (n + 1)
# DFS 수행
dfs(graph, 1, visited)
# 1번을 제외한 바이러스에 걸린 컴퓨터 수 계산
print(sum(visited) - 1)  # 1번 컴퓨터는 제외

