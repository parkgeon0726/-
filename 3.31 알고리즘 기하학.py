#3.31 알고리즘 기하학 관련5문제

#https://www.acmicpc.net/problem/10216 문제
import sys
def main():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        nodes = [tuple(map(int, data[idx+i*3:idx+(i+1)*3])) for i in range(N)]
        idx += N*3
        parent = list(range(N))
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # 경로 압축
                u = parent[u]
            return u
        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root != v_root:
                parent[v_root] = u_root  # 랭크 최적화 생략
        # 모든 진영 쌍 비교
        for i in range(N):
            x1, y1, r1 = nodes[i]
            for j in range(i+1, N):
                x2, y2, r2 = nodes[j]
                dx = x1 - x2
                dy = y1 - y2
                if dx*dx + dy*dy <= (r1 + r2)**2:
                    union(i, j)
        # 고유 루트 개수 카운트
        print(len({find(i) for i in range(N)}))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/1485 문제
import sys
from itertools import combinations
def is_square(points):
    dists = []
    # 모든 점 쌍 간의 거리 제곱 계산
    for (x1, y1), (x2, y2) in combinations(points, 2):
        dx = x1 - x2
        dy = y1 - y2
        dist_sq = dx*dx + dy*dy
        dists.append(dist_sq)
    dists.sort()
    # 정사각형 조건 검사
    return (
        len(dists) == 6 and
        dists[0] == dists[1] == dists[2] == dists[3] and  # 네 변 길이 동일
        dists[4] == dists[5] and  # 두 대각선 길이 동일
        dists[0] * 2 == dists[4]  # 변과 대각선 관계 확인
    )
def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for _ in range(T):
        points = []
        for __ in range(4):
            x = int(input[idx])
            y = int(input[idx+1])
            points.append((x, y))
            idx +=2
        print(1 if is_square(points) else 0)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/14264 문제
import math
L = int(input())
print(math.sqrt(3) / 4 * L * L)

#https://www.acmicpc.net/problem/15610 문제
import math
# 입력: 정육면체의 면적
a = int(input())
# 한 변의 길이 계산
side_length = math.sqrt(a)
# 총 전선 길이 계산 (정사각형의 둘레)
total_wiring_length = 4 * side_length
# 결과 출력
print(f"{total_wiring_length:.6f}")

#https://www.acmicpc.net/problem/8723 문제제
a, b, c = map(int, input().split())
if a == b == c:
    print(2)
else:
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print(1)
    else:
        print(0)