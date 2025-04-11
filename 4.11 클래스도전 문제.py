#4.11 클래스 관련5문제

#https://www.acmicpc.net/problem/11727 문제
def count_tiling_ways(n):
    MOD = 10007
    # 기본 케이스 처리
    if n == 1:
        return 1
    elif n == 2:
        return 3
    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    # 점화식을 사용하여 DP 배열 채우기
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD
    return dp[n]
def main():
    n = int(input())
    result = count_tiling_ways(n)
    print(result)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/17626 문제
import math
def four_squares(n):
    # 1개의 제곱수로 표현 가능한 경우
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    # 2개의 제곱수로 표현 가능한 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - pow(i, 2))) == math.sqrt(n - pow(i, 2)):
            return 2
    # 3개의 제곱수로 표현 가능한 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - pow(i, 2))) + 1):
            if int(math.sqrt(n - pow(i, 2) - pow(j, 2))) == math.sqrt(n - pow(i, 2) - pow(j, 2)):
                return 3
    # 나머지는 모두 4개의 제곱수로 표현 가능
    return 4
n = int(input())
print(four_squares(n))

#https://www.acmicpc.net/problem/1012 문제
import sys
sys.setrecursionlimit(10000)  # 재귀 제한 설정
def dfs(x, y):
    # 상하좌우 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 현재 위치를 방문했다고 표시 (0으로 변경)
    field[y][x] = 0
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배추밭 범위 내에 있고, 아직 방문하지 않은 배추가 있는지 확인
        if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
            dfs(nx, ny)
T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    M, N, K = map(int, input().split())  # 가로길이, 세로길이, 배추 개수
    # 배추밭 초기화
    field = [[0] * M for _ in range(N)]
    # 배추 위치 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1  # 배추 위치를 1로 표시
    count = 0  # 지렁이 수 (연결된 컴포넌트 수)
    # 모든 위치를 탐색
    for y in range(N):
        for x in range(M):
            # 배추가 있고 아직 방문하지 않았다면
            if field[y][x] == 1:
                dfs(x, y)  # DFS로 연결된 모든 배추를 방문
                count += 1  # 지렁이 수 증가
    print(count)

#https://www.acmicpc.net/problem/1260
from collections import deque
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
def bfs(graph, start, visited):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
# 정점의 개수 N, 간선의 개수 M, 시작 정점 V 입력받기
n, m, v = map(int, input().split())
# 그래프 초기화 (1부터 n까지의 정점)
graph = [[] for _ in range(n+1)]
# 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 간선이므로 양쪽에 추가
    graph[a].append(b)
    graph[b].append(a)
# 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
for i in range(1, n+1):
    graph[i].sort()
# DFS 수행
visited = [False] * (n+1)
dfs(graph, v, visited)
print()  # 줄 바꿈
# BFS 수행
visited = [False] * (n+1)
bfs(graph, v, visited)

#https://www.acmicpc.net/problem/1541 문제
expression = input().split('-')
sum_parts = []
for part in expression:
    nums = part.split('+')
    total = sum(map(int, nums))
    sum_parts.append(total)
result = sum_parts[0]
for num in sum_parts[1:]:
    result -= num
print(result)

