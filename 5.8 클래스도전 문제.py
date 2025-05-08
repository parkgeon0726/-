#5.8 클래스도전 관련5문제

#https://www.acmicpc.net/problem/15650 문제
from itertools import combinations
n, m = map(int, input().split())
for comb in combinations(range(1, n+1), m):
    print(*comb)

#https://www.acmicpc.net/problem/15652 문제
from itertools import combinations_with_replacement
n, m = map(int, input().split())
for combo in combinations_with_replacement(range(1, n+1), m):
    print(' '.join(map(str, combo)))

#https://www.acmicpc.net/problem/15654 문제
import itertools
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
for permutation in itertools.permutations(numbers, m):
    print(' '.join(map(str, permutation)))

#https://www.acmicpc.net/problem/15663 문제
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
used = [False] * n
path = []
def backtrack():
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    for i in range(n):
        if not used[i]:
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False
backtrack()

#https://www.acmicpc.net/problem/15666 문제
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(list(set(nums)))  # 중복 제거 후 정렬
selected = []
def backtrack(start):
    if len(selected) == m:
        print(' '.join(map(str, selected)))
        return
    for i in range(start, len(nums)):
        selected.append(nums[i])
        backtrack(i)  # 비내림차순을 위해 현재 인덱스부터 시작
        selected.pop()
backtrack(0)
