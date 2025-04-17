#4.17 클래스도전 관련5문제

#https://www.acmicpc.net/problem/1697 문제
from collections import deque
def bfs(n, k):
    # 최대 위치 제한
    max_pos = 100000
    # 방문 배열 초기화 (-1은 방문하지 않음을 의미)
    visited = [-1] * (max_pos + 1)
    # 시작 위치 설정
    queue = deque([n])
    visited[n] = 0
    while queue:
        pos = queue.popleft()
        # 동생을 찾은 경우
        if pos == k:
            return visited[pos]
        # 세 가지 이동 방향 확인
        for next_pos in (pos - 1, pos + 1, pos * 2):
            # 유효한 위치이고 아직 방문하지 않은 경우
            if 0 <= next_pos <= max_pos and visited[next_pos] == -1:
                visited[next_pos] = visited[pos] + 1
                queue.append(next_pos)
    return -1  # 도달할 수 없는 경우 (실제로는 발생하지 않음)
# 입력 받기
n, k = map(int, input().split())
# BFS 실행 및 결과 출력
print(bfs(n, k))

#https://www.acmicpc.net/problem/2178 문제
from collections import deque
import sys
def main():
    # 입력 받기
    n, m = map(int, sys.stdin.readline().split())
    maze = []
    for _ in range(n):
        row = sys.stdin.readline().strip()
        maze.append([int(c) for c in row])
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS 초기화
    queue = deque()
    queue.append((0, 0))  # 시작 위치 (0-based)
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위 내인지 확인
            if 0 <= nx < n and 0 <= ny < m:
                # 이동 가능한 칸이면
                if maze[nx][ny] == 1:
                    # 도착지에 도달한 경우
                    if nx == n-1 and ny == m-1:
                        print(maze[x][y] + 1)
                        return
                    # 이동 거리 갱신 및 큐에 추가
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
    # 문제 조건상 도달 못 하는 경우는 없음
    print(-1)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/2667 문제
import sys
sys.setrecursionlimit(10**6)  # 재귀 제한을 늘립니다
def dfs(grid, x, y, n):
    # 범위를 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    # 집이 없거나 이미 방문한 경우 종료
    if grid[x][y] == 0:
        return 0
    # 현재 집 방문 처리
    grid[x][y] = 0
    count = 1
    # 상하좌우 이동
    count += dfs(grid, x+1, y, n)  # 아래
    count += dfs(grid, x-1, y, n)  # 위
    count += dfs(grid, x, y+1, n)  # 오른쪽
    count += dfs(grid, x, y-1, n)  # 왼쪽
    return count
def solve_dfs():
    # 입력 처리
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().strip()))
        grid.append(row)
    # 단지 찾기
    complexes = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                house_count = dfs(grid, i, j, n)
                complexes.append(house_count)
    # 결과 출력
    complexes.sort()  # 오름차순 정렬
    print(len(complexes))  # 총 단지수
    for count in complexes:
        print(count)  # 각 단지내 집의 수
solve_dfs()

#https://www.acmicpc.net/problem/5525 문제
import sys
def solve():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    answer = 0
    i = 0
    count = 0
    while i < m - 2:  # i+2가 문자열 범위를 벗어나지 않도록
        if s[i:i+3] == 'IOI':
            count += 1
            i += 2  # 다음 패턴 확인을 위해 2칸 이동
            if count == n:
                answer += 1
                count -= 1  # 다음 P_N 패턴을 찾기 위해 count 감소
        else:
            i += 1  # 패턴이 아니면 1칸 이동
            count = 0  # 패턴이 끊겼으므로 count 초기화
    return answer
print(solve())

#https://www.acmicpc.net/problem/6064 문제
import sys
import math
def solve():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        M = int(input[idx])
        N = int(input[idx+1])
        x = int(input[idx+2])
        y = int(input[idx+3])
        idx += 4
        d = math.gcd(M, N)
        if (y - x) % d != 0:
            print(-1)
            continue
        a = M // d
        m = N // d
        b = (y - x) // d
        try:
            inv = pow(a, -1, m)
        except ValueError:
            print(-1)
            continue
        t0 = (b * inv) % m
        k = x + t0 * M
        print(k)
if __name__ == "__main__":
    solve()

#https://www.acmicpc.net/problem/11286 문제
import heapq
import sys
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    heap = []
    result = []
    for i in range(1, n + 1):
        x = int(data[i])
        if x != 0:
            heapq.heappush(heap, (abs(x), x))
        else:
            if heap:
                result.append(str(heapq.heappop(heap)[1]))
            else:
                result.append('0')
    print('\n'.join(result))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/11403 문제
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for row in graph:
    print(' '.join(map(str, row)))

#https://www.acmicpc.net/problem/14940 문제
import sys
from collections import deque
def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    m = int(input[idx+1])
    idx += 2
    map_data = []
    target = None
    for i in range(n):
        row = list(map(int, input[idx:idx+m]))
        idx += m
        if 2 in row:
            target = (i, row.index(2))
        map_data.append(row)
    # 거리 배열 초기화
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 목표지점 설정
    tx, ty = target
    dist[tx][ty] = 0
    q.append((tx, ty))
    # 원래 0인 곳은 거리 0으로 설정
    for i in range(n):
        for j in range(m):
            if map_data[i][j] == 0:
                dist[i][j] = 0
    # BFS 수행
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if map_data[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    # 결과 출력
    for row in dist:
        print(' '.join(map(str, row)))
if __name__ == "__main__":
    main()


