#4.14 클래스도전 관련5문제

#https://www.acmicpc.net/problem/1927 문제
import heapq
import sys
# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline
# 연산의 개수 N 입력받기
N = int(input())
# 최소 힙 초기화
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:  # 가장 작은 값 출력 및 제거
        if len(heap) == 0:  # 힙이 비어있는 경우
            print(0)
        else:  # 힙에 값이 있는 경우
            print(heapq.heappop(heap))
    else:  # 힙에 값 추가
        heapq.heappush(heap, x)

#https://www.acmicpc.net/problem/2630 문제
def solution(n, paper):
    # 하얀색과 파란색 색종이의 개수를 저장할 변수
    white_count = 0
    blue_count = 0
    def divide_and_count(x, y, size):
        nonlocal white_count, blue_count
        # 현재 영역의 첫 번째 색상
        color = paper[x][y]
        uniform = True
        # 현재 영역이 모두 같은 색인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != color:
                    uniform = False
                    break
            if not uniform:
                break
        # 모두 같은 색이면 해당 색상의 색종이 개수 증가
        if uniform:
            if color == 0:
                white_count += 1
            else:
                blue_count += 1
        else:
            # 같은 색이 아니면 네 개 영역으로 분할
            half = size // 2
            divide_and_count(x, y, half)                  # 좌상단
            divide_and_count(x, y + half, half)           # 우상단
            divide_and_count(x + half, y, half)           # 좌하단
            divide_and_count(x + half, y + half, half)    # 우하단
    # 전체 종이에 대해 함수 호출
    divide_and_count(0, 0, n)
    return white_count, blue_count
# 입력 처리
n = int(input())
paper = []
for _ in range(n):
    row = list(map(int, input().split()))
    paper.append(row)
# 결과 출력
white, blue = solution(n, paper)
print(white)
print(blue)

#https://www.acmicpc.net/problem/2805 문제
import sys
def find_max_height(trees, m):
    """
    적어도 m미터의 나무를 얻을 수 있는 절단기의 최대 높이를 반환합니다.
    """
    start = 0
    end = max(trees)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        # 절단기 높이가 mid일 때 얻을 수 있는 나무의 양 계산
        wood_amount = sum(tree - mid for tree in trees if tree > mid)
        if wood_amount >= m:
            # 현재 높이에서 충분한 나무를 얻을 수 있으므로, 최대 높이를 갱신합니다.
            result = mid
            start = mid + 1
        else:
            # 현재 높이에서 얻을 수 있는 나무가 부족하므로, 높이를 낮춥니다.
            end = mid - 1
    return result
# 입력 받기
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
# 결과 계산 및 출력
max_height = find_max_height(trees, m)
print(max_height)

#https://www.acmicpc.net/problem/11279 문제
import sys
import heapq
def main():
    n = int(sys.stdin.readline())
    heap = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x == 0:
            print(-heapq.heappop(heap) if heap else 0)
        else:
            heapq.heappush(heap, -x)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/11724 문제
import sys
from collections import deque
def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * (n+1)
    count = 0
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            count += 1
    print(count)
if __name__ == "__main__":
    main()

