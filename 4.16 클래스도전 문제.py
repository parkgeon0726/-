#4.16 클래스도전 관련5문제

#https://www.acmicpc.net/problem/18111 문제
import sys
def main():
    N, M, B = map(int, sys.stdin.readline().split())
    freq = [0] * 257
    # 높이 분포 계산
    for _ in range(N):
        for h in map(int, sys.stdin.readline().split()):
            freq[h] += 1
    min_time = float('inf')
    best_h = 0
    # 높은 높이부터 역순 탐색
    for target_h in range(256, -1, -1):
        total_remove = 0
        total_add = 0
        # 모든 높이에 대해 차이 계산
        for current_h in range(257):
            cnt = freq[current_h]
            if current_h > target_h:
                total_remove += (current_h - target_h) * cnt
            else:
                total_add += (target_h - current_h) * cnt
        # 작업 가능성 검증
        if total_add <= B + total_remove:
            current_time = total_remove * 2 + total_add
            if current_time < min_time:
                min_time = current_time
                best_h = target_h    
    print(min_time, best_h)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/18870 문제
import sys
def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    nums = list(map(int, input[1:n+1]))
    # 중복 제거 및 정렬
    sorted_nums = sorted(set(nums))
    # 좌표 압축 딕셔너리 생성
    compression = {num: idx for idx, num in enumerate(sorted_nums)}
    # 결과 계산
    result = [compression[num] for num in nums]
    print(' '.join(map(str, result)))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/21736 문제
import sys
from collections import deque
def main():
    # 입력 처리
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    start = None
    # 그리드 구성 및 시작 위치 탐색
    for i in range(n):
        row = list(sys.stdin.readline().strip())
        grid.append(row)
        if 'I' in row:
            for j in range(m):
                if row[j] == 'I':
                    start = (i, j)
                    break
    # BFS 초기 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    count = 0
    if start:
        x, y = start
        queue.append((x, y))
        grid[x][y] = 'X'  # 시작 지점 방문 처리
        # BFS 탐색 수행
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] != 'X':
                        if grid[nx][ny] == 'P':
                            count += 1
                        grid[nx][ny] = 'X'  # 방문 처리
                        queue.append((nx, ny))
    # 결과 출력
    print('TT' if count == 0 else count)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/30804 문제
import sys
from collections import defaultdict
def main():
    n = int(sys.stdin.readline())
    fruits = list(map(int, sys.stdin.readline().split()))
    counts = defaultdict(int)
    left = 0
    max_length = 0
    distinct = 0
    for right in range(n):
        current = fruits[right]
        if counts[current] == 0:
            distinct += 1
        counts[current] += 1
        while distinct > 2:
            left_fruit = fruits[left]
            counts[left_fruit] -= 1
            if counts[left_fruit] == 0:
                distinct -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    print(max_length)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/1389 문제
import sys
from collections import deque
def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n+1)]  # 1-based indexing
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    min_bacon = float('inf')
    answer = 0
    for user in range(1, n+1):
        distance = [-1] * (n+1)
        distance[user] = 0
        q = deque([user])
        while q:
            current = q.popleft()
            for neighbor in adj[current]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[current] + 1
                    q.append(neighbor)
        total = sum(distance[1:])  # 모든 사용자 거리 합산
        if total < min_bacon or (total == min_bacon and user < answer):
            min_bacon = total
            answer = user
    print(answer)
if __name__ == "__main__":
    main()
