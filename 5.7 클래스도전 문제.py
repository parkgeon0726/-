#5.7 클래스도전 관련10문제

#https://www.acmicpc.net/problem/1074 문제
def solve(n, r, c):
    # 기저 조건: 크기가 1x1인 경우
    if n == 0:
        return 0
    half = 2 ** (n - 1)  # 한 변의 절반 길이
    # 2사분면(왼쪽 위)
    if r < half and c < half:
        return solve(n - 1, r, c)
    # 1사분면(오른쪽 위)
    elif r < half and c >= half:
        return half * half + solve(n - 1, r, c - half)
    # 3사분면(왼쪽 아래)
    elif r >= half and c < half:
        return 2 * half * half + solve(n - 1, r - half, c)
    # 4사분면(오른쪽 아래)
    else:
        return 3 * half * half + solve(n - 1, r - half, c - half)
# 입력 받기
n, r, c = map(int, input().split())
print(solve(n, r, c))

#https://www.acmicpc.net/problem/1931 문제
import sys
def main():
    n = int(sys.stdin.readline())
    meetings = []
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        meetings.append((s, e))
    # 끝나는 시간 기준 오름차순, 시작 시간 기준 오름차순 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    count = 0
    current_end = 0
    for s, e in meetings:
        if s >= current_end:
            count += 1
            current_end = e
    print(count)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/5430 문제
import sys
from collections import deque
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        p = sys.stdin.readline().strip()
        n = int(sys.stdin.readline())
        arr_str = sys.stdin.readline().strip()
        if arr_str == '[]':
            dq = deque()
        else:
            dq = deque(map(int, arr_str[1:-1].split(',')))
        reverse = False
        error = False
        for cmd in p:
            if cmd == 'R':
                reverse = not reverse
            elif cmd == 'D':
                if not dq:
                    error = True
                    break
                if reverse:
                    dq.pop()
                else:
                    dq.popleft()
        if error:
            print("error")
        else:
            if reverse:
                dq.reverse()
            print(f"[{','.join(map(str, dq))}]" if dq else "[]")
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/7576 문제
from collections import deque
import sys
def main():
    # 더 빠른 입력 처리를 위해 sys.stdin.readline 사용
    m, n = map(int, sys.stdin.readline().split())
    box = []
    queue = deque()
    # 토마토 상자 정보 입력 및 익은 토마토 위치 저장
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        box.append(row)
        for j in range(m):
            if row[j] == 1:
                queue.append((i, j))
    # 상하좌우 이동 방향
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # BFS 실행
    while queue:
        x, y = queue.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 체크 및 익지 않은 토마토 확인
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1  # 날짜를 기록
                queue.append((nx, ny))
    # 익지 않은 토마토가 남아있는지 확인 및 최대 날짜 계산
    max_days = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1  # 익지 않은 토마토가 있다면 -1 반환
            max_days = max(max_days, box[i][j])
    return max_days - 1  # 초기 상태가 1이므로 1을 빼줌
print(main())

#https://www.acmicpc.net/problem/7569 문제
from collections import deque
import sys
input = sys.stdin.readline
# 입력 받기
M, N, H = map(int, input().split())  # M: 가로, N: 세로, H: 높이
tomato = []
# 3차원 배열 생성
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, input().split())))
    tomato.append(layer)
# 익은 토마토 위치 찾기
queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                queue.append((h, n, m))  # (높이, 세로, 가로)
# 6방향 이동 (위, 아래, 앞, 뒤, 왼쪽, 오른쪽)
dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]
# BFS 수행
while queue:
    h, n, m = queue.popleft()
    for i in range(6):
        nh = h + dh[i]
        nn = n + dn[i]
        nm = m + dm[i]
        # 범위 체크
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            # 익지 않은 토마토가 있으면 익히기
            if tomato[nh][nn][nm] == 0:
                tomato[nh][nn][nm] = tomato[h][n][m] + 1  # 현재 위치의 값 + 1
                queue.append((nh, nn, nm))
# 결과 계산
max_day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:  # 익지 않은 토마토가 있다면
                print(-1)
                exit(0)
            max_day = max(max_day, tomato[h][n][m])
# 결과 출력 (최대 값이 1이면 처음부터 모든 토마토가 익어있었음)
print(max_day - 1)

#https://www.acmicpc.net/problem/10026 문제
import sys
from collections import deque
import copy
# 빠른 입력을 위해 sys.stdin.readline 사용
n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))
# 적록색약 버전의 그리드 만들기 (G를 R로 변환)
colorblind_grid = copy.deepcopy(grid)
for i in range(n):
    for j in range(n):
        if colorblind_grid[i][j] == 'G':
            colorblind_grid[i][j] = 'R'
# 상하좌우 이동을 위한 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# BFS 함수: 같은 색상의 연결된 구역 탐색
def bfs(x, y, grid, visited):
    queue = deque([(x, y)])
    color = grid[x][y]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
# 일반 사람이 보는 구역 수 계산
normal_visited = [[False] * n for _ in range(n)]
normal_count = 0
for i in range(n):
    for j in range(n):
        if not normal_visited[i][j]:
            bfs(i, j, grid, normal_visited)
            normal_count += 1
# 적록색약인 사람이 보는 구역 수 계산
colorblind_visited = [[False] * n for _ in range(n)]
colorblind_count = 0
for i in range(n):
    for j in range(n):
        if not colorblind_visited[i][j]:
            bfs(i, j, colorblind_grid, colorblind_visited)
            colorblind_count += 1
print(normal_count, colorblind_count)

#https://www.acmicpc.net/problem/16928 문제
from collections import deque
import sys
def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    ladders = {}
    for _ in range(n):
        x, y = map(int, input().split())
        ladders[x] = y
    snakes = {}
    for _ in range(m):
        u, v = map(int, input().split())
        snakes[u] = v
    visited = [False] * 101
    queue = deque([(1, 0)])
    visited[1] = True
    while queue:
        pos, rolls = queue.popleft()
        if pos == 100:
            print(rolls)
            return
        for dice in range(1, 7):
            new_pos = pos + dice
            if new_pos > 100:
                continue
            # 사다리와 뱀 처리
            while True:
                if new_pos in ladders:
                    new_pos = ladders[new_pos]
                elif new_pos in snakes:
                    new_pos = snakes[new_pos]
                else:
                    break
            if new_pos <= 100 and not visited[new_pos]:
                visited[new_pos] = True
                queue.append((new_pos, rolls + 1))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/7662 문제
import sys
import heapq
from collections import defaultdict
def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        k = int(input[ptr])
        ptr += 1
        min_heap = []
        max_heap = []
        count = defaultdict(int)
        for __ in range(k):
            op = input[ptr]
            num = input[ptr+1]
            ptr +=2
            if op == 'I':
                n = int(num)
                heapq.heappush(min_heap, n)
                heapq.heappush(max_heap, -n)
                count[n] +=1
            else:
                if num == '1':
                    while max_heap and count[-max_heap[0]] ==0:
                        heapq.heappop(max_heap)
                    if max_heap:
                        val = -heapq.heappop(max_heap)
                        count[val] -=1
                else:
                    while min_heap and count[min_heap[0]] ==0:
                        heapq.heappop(min_heap)
                    if min_heap:
                        val = heapq.heappop(min_heap)
                        count[val] -=1
        # Clean up heaps to find valid max and min
        while max_heap and count[-max_heap[0]] ==0:
            heapq.heappop(max_heap)
        while min_heap and count[min_heap[0]] ==0:
            heapq.heappop(min_heap)
        if not max_heap or not min_heap:
            print("EMPTY")
        else:
            max_val = -max_heap[0]
            min_val = min_heap[0]
            print(f"{max_val} {min_val}")
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/9019 문제
import sys
from collections import deque

def bfs(start, target):
    visited = [False] * 10000
    queue = deque()
    queue.append((start, ""))
    visited[start] = True
    
    while queue:
        num, path = queue.popleft()
        if num == target:
            return path
        
        # D 연산
        next_num = (num * 2) % 10000
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + 'D'))
        
        # S 연산
        next_num = (num - 1) % 10000
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + 'S'))
        
        # L 연산
        next_num = (num % 1000) * 10 + num // 1000
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + 'L'))
        
        # R 연산
        next_num = (num % 10) * 1000 + num // 10
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + 'R'))
    
    return ""

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A, B))


#https://www.acmicpc.net/problem/14500 문제
import sys
sys.setrecursionlimit(15000)  # 재귀 깊이 제한 확장
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_val = max(map(max, grid))  # 그리드 최대값 미리 계산
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False]*M for _ in range(N)]
    max_sum = 0
    def dfs(x, y, depth, current):
        nonlocal max_sum
        # 남은 블록 최대값 기반 조기 종료
        if current + max_val * (4 - depth) <= max_sum:
            return
        # 테트로미노 완성 시 최대값 갱신
        if depth == 4:
            max_sum = max(max_sum, current)
            return
        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # T-형 처리 (2단계에서 원점 재방문)
                if depth == 2:
                    visited[nx][ny] = True
                    dfs(x, y, depth+1, current + grid[nx][ny])
                    visited[nx][ny] = False
                # 일반적인 DFS 탐색
                visited[nx][ny] = True
                dfs(nx, ny, depth+1, current + grid[nx][ny])
                visited[nx][ny] = False
    # 모든 시작점에 대해 탐색
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, grid[i][j])
            visited[i][j] = False
    print(max_sum)
if __name__ == "__main__":
    main()
