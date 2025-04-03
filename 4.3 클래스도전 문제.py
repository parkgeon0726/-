#4.3 클래스도전 관련25문제

#https://www.acmicpc.net/problem/1181 문제
# 입력 받기
import sys
input = sys.stdin.read
data = input().splitlines()
N = int(data[0])  # 첫째 줄에 단어의 개수 N
words = data[1:]  # 둘째 줄부터 N개의 단어
# 중복 제거
unique_words = list(set(words))
# 정렬: 길이 -> 사전 순
sorted_words = sorted(unique_words, key=lambda x: (len(x), x))
# 출력
print("\n".join(sorted_words))

#https://www.acmicpc.net/problem/1436 문제
def find_nth_apocalyptic_number(n):
    count = 0
    num = 666  # 첫 종말의 수 666에서 시작
    while True:
        if '666' in str(num):  # 숫자에 666 포함 여부 확인
            count += 1
            if count == n:
                return num
        num += 1  # 다음 숫자 검사
# 입력 처리 및 실행
N = int(input())
print(find_nth_apocalyptic_number(N))

#https://www.acmicpc.net/problem/1676 문제
def count_trailing_zeros(n):
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count
# 입력 처리
N = int(input())
print(count_trailing_zeros(N))

#https://www.acmicpc.net/problem/2751 문제
import sys
def main():
    data = sys.stdin.read().splitlines()
    numbers = list(map(int, data[1:]))  # 첫 줄 제외 후 숫자 변환
    numbers.sort()
    print('\n'.join(map(str, numbers)))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/7568 문제
import sys
def calculate_ranks(people):
    n = len(people)
    ranks = [1] * n  # 초기 등수 1로 설정
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # i번째 사람이 j번째 사람보다 덩치가 큰 경우
            if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
                ranks[j] += 1  # j의 등수 하락
    return ranks
# 입력 처리
data = sys.stdin.read().splitlines()
N = int(data[0])
people = [tuple(map(int, line.split())) for line in data[1:N+1]]
# 등수 계산 및 출력
result = calculate_ranks(people)
print(' '.join(map(str, result)))

#https://www.acmicpc.net/problem/10814 문제
import sys
def sort_members():
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])  # 첫 번째 줄은 회원 수
    members = []  # 회원 정보를 저장할 리스트
    # 회원 정보 입력
    for i in range(1, N + 1):
        age, name = data[i].split()
        members.append((int(age), i, name))  # 나이, 가입 순서, 이름 저장
    # 정렬: 나이 오름차순 -> 가입 순서 오름차순
    members.sort(key=lambda x: (x[0], x[1]))
    # 결과 출력
    for age, _, name in members:
        print(age, name)
# 함수 실행
sort_members()

#https://www.acmicpc.net/problem/11650 문제
import sys
def main():
    # 전체 입력 데이터 읽기
    data = sys.stdin.read().splitlines()
    N = int(data[0])  # 첫 줄: 점의 개수
    # 좌표 파싱 (x, y 튜플 리스트)
    points = [tuple(map(int, line.split())) for line in data[1:N+1]]
    # 정렬: x 오름차순 → y 오름차순
    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
    # 결과 출력
    for x, y in sorted_points:
        print(x, y)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/11651 문제
import sys
def main():
    # 전체 입력 데이터 일괄 읽기
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    # 좌표 데이터 파싱 (y, x 순서 저장)
    points = [tuple(map(int, line.split())) for line in data[1:N+1]]
    # 정렬 기준: y 오름차순 → x 오름차순
    points.sort(key=lambda p: (p[1], p[0]))
    # 결과 출력
    for x, y in points:
        print(x, y)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/1018 문제
import sys
def main():
    # 입력 처리
    input = sys.stdin.read().splitlines()
    N, M = map(int, input[0].split())
    board = input[1:N+1]
    min_count = float('inf')  # 최소 변경 횟수 초기화
    # 모든 가능한 시작점 탐색
    for i in range(N - 7):
        for j in range(M - 7):
            count_w = 0  # W 시작 패턴 기준 변경 횟수
            count_b = 0  # B 시작 패턴 기준 변경 횟수
            # 8x8 영역 검사
            for x in range(8):
                for y in range(8):
                    current = board[i+x][j+y]
                    expected_w = 'W' if (x+y) % 2 == 0 else 'B'
                    expected_b = 'B' if (x+y) % 2 == 0 else 'W'
                    if current != expected_w:
                        count_w += 1
                    if current != expected_b:
                        count_b += 1
            # 최소값 갱신
            current_min = min(count_w, count_b)
            if current_min < min_count:
                min_count = current_min
    print(min_count)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/1920 문제
import sys
def main():
    input = sys.stdin.readline
    # N 입력 받기
    N = int(input())
    # 집합 A 생성
    A = set(map(int, input().split()))
    # M 입력 받기
    M = int(input())
    # 확인할 숫자들 리스트
    check_nums = list(map(int, input().split()))
    # 각 숫자 확인 후 결과 출력
    for num in check_nums:
        print(1 if num in A else 0)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/2164 문제
n = int(input())
if n == 1:
    print(1)
else:
    power = 1
    while power * 2 <= n:
        power *= 2
    print(2*(n - power) if n != power else n)

#https://www.acmicpc.net/problem/2839 문제
n = int(input())
count = 0
# 5kg 봉지 최대 사용
while n >= 0:
    if n % 5 == 0:  # 5kg로 나누어 떨어지면 최적해
        count += n // 5
        print(count)
        exit()
    n -= 3  # 5kg로 안 되면 3kg 1개 사용
    count += 1
else:
    print(-1)

#https://www.acmicpc.net/problem/4949 문제
import sys
def check_balance(s):
    stack = []
    pairs = {')': '(', ']': '['}
    for char in s:
        if char in '([':  # 여는 괄호 처리
            stack.append(char)
        elif char in ')]':  # 닫는 괄호 처리
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0  # 스택이 비어있어야 성공
while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == '.':  # 종료 조건
        break
    filtered = [c for c in line if c in '()[]']  # 괄호만 필터링
    print('yes' if check_balance(filtered) else 'no')

#https://www.acmicpc.net/problem/9012 문제
import sys
def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
def main():
    input = sys.stdin.read().splitlines()
    T = int(input[0].strip())
    results = []
    for line in input[1:T+1]:  # T개만 처리 (나머지 무시)
        line = line.strip()
        if not line:  # 빈 줄 건너뛰기
            continue
        results.append("YES" if is_vps(line) else "NO")
    print('\n'.join(results))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/10773 문제
import sys
def main():
    K = int(sys.stdin.readline())
    stack = []
    for _ in range(K):
        num = int(sys.stdin.readline())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    print(sum(stack))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/10816 문제
import sys
from collections import Counter
def main():
    # 전체 입력을 한 번에 읽기
    lines = sys.stdin.read().splitlines()
    N = int(lines[0])
    numbers = list(map(int, lines[1].split()))
    M = int(lines[2])
    queries = list(map(int, lines[3].split()))
    # 숫자 카운팅
    count = Counter(numbers)
    # 결과 생성 및 출력
    result = [str(count.get(q, 0)) for q in queries]
    print(' '.join(result))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/10828 문제
import sys
def main():
    n = int(sys.stdin.readline())
    stack = []
    result = []
    for _ in range(n):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == 'push':
            stack.append(int(command[1]))
        elif command[0] == 'pop':
            result.append(str(stack.pop()) if stack else '-1')
        elif command[0] == 'size':
            result.append(str(len(stack)))
        elif command[0] == 'empty':
            result.append('1' if not stack else '0')
        elif command[0] == 'top':
            result.append(str(stack[-1]) if stack else '-1')
    print('\n'.join(result))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/10845 문제
import sys
from collections import deque
def main():
    input = sys.stdin.read().splitlines()
    n = int(input[0])
    q = deque()
    result = []
    for line in input[1:n+1]:
        cmd = line.split()
        if cmd[0] == 'push':
            q.append(int(cmd[1]))
        elif cmd[0] == 'pop':
            result.append(str(q.popleft()) if q else '-1')
        elif cmd[0] == 'size':
            result.append(str(len(q)))
        elif cmd[0] == 'empty':
            result.append('1' if not q else '0')
        elif cmd[0] == 'front':
            result.append(str(q[0]) if q else '-1')
        elif cmd[0] == 'back':
            result.append(str(q[-1]) if q else '-1')
    print('\n'.join(result))
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/11866 문제
from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n+1))
result = []
while q:
    q.rotate(-(k-1))  # 왼쪽으로 k-1번 회전 = 앞의 k-1개 요소 뒤로 이동
    result.append(str(q.popleft()))
print(f"<{', '.join(result)}>")

#https://www.acmicpc.net/problem/18110 문제
import sys
input = sys.stdin.readline
# 반올림 함수 구현 (사사오입 원칙)
def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)
# 입력 처리
n = int(input())
# 난이도 의견이 없는 경우
if n == 0:
    print(0)
else:
    # 난이도 의견 입력 받기
    level_opinions = []
    for _ in range(n):
        level_opinions.append(int(input()))
    # 정렬
    level_opinions.sort()
    # 절사할 수 계산 (15% 반올림)
    cut = my_round(n * 0.15)
    # 절사된 의견으로 평균 계산
    trimmed_opinions = level_opinions[cut:n-cut]
    average = sum(trimmed_opinions) / len(trimmed_opinions)
    # 최종 난이도 출력
    print(my_round(average))

#https://www.acmicpc.net/problem/1929 문제
def sieve(max_num):
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            sieve[i*i : max_num+1 : i] = [False] * len(sieve[i*i : max_num+1 : i])
    return sieve
m, n = map(int, input().split())
primes = sieve(n)
for num in range(m, n + 1):
    if primes[num]:
        print(num)

#https://www.acmicpc.net/problem/1966 문제
from collections import deque
import sys
def find_print_order():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        priorities = list(map(int, sys.stdin.readline().split()))
        q = deque([(val, idx) for idx, val in enumerate(priorities)])
        count = 0
        while q:
            current = q.popleft()
            if any(current[0] < item[0] for item in q):
                q.append(current)
            else:
                count += 1
                if current[1] == m:
                    print(count)
                    break
if __name__ == "__main__":
    find_print_order()

#https://www.acmicpc.net/problem/1654 문제
import sys
def find_max_length():
    k, n = map(int, sys.stdin.readline().split())
    cables = [int(sys.stdin.readline()) for _ in range(k)]
    start, end = 1, max(cables)
    while start <= end:
        mid = (start + end) // 2
        total = sum(cable // mid for cable in cables)
        if total >= n:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
if __name__ == "__main__":
    find_max_length()

#https://www.acmicpc.net/problem/1874 문제
import sys
def validate_stack_sequence():
    n = int(sys.stdin.readline())
    sequence = [int(sys.stdin.readline()) for _ in range(n)]
    stack = []
    current = 1
    result = []
    for target in sequence:
        # 현재 타겟까지 숫자 생성
        while current <= target:
            stack.append(current)
            result.append('+')
            current += 1
        # 스택 최상위 요소 검증
        if stack and stack[-1] == target:
            stack.pop()
            result.append('-')
        else:
            print("NO")
            return
    print('\n'.join(result))
if __name__ == "__main__":
    validate_stack_sequence()

#https://www.acmicpc.net/problem/2108 문제
import sys
from collections import Counter
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
# 산술평균 계산 (소수점 첫째 자리 반올림)
print(round(sum(numbers) / n))
# 중앙값 계산 (오름차순 정렬 후 중간값)
numbers.sort()
print(numbers[len(numbers) // 2])
# 최빈값 계산 (최다 등장값 중 두 번째 작은 수)
count = Counter(numbers)
max_freq = max(count.values())
modes = sorted([k for k, v in count.items() if v == max_freq])
print(modes[1] if len(modes) > 1 else modes[0])
# 범위 계산 (최대값 - 최소값)
print(max(numbers) - min(numbers))