#4.2 클래스도전 관련문제

#https://www.acmicpc.net/problem/30802 문제
def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    sizes = list(map(int, input[1:7]))
    T, P = map(int, input[7:9])
    # 티셔츠 계산
    tshirt_bundles = sum((-size // T) * -1 for size in sizes)
    # 펜 계산
    pen_bundles = N // P
    pen_individual = N % P
    print(tshirt_bundles)
    print(pen_bundles, pen_individual)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/1978 문제
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_primes(numbers):
    prime_count = 0
    for number in numbers:
        if is_prime(number):
            prime_count += 1
    return prime_count
# 입력 처리
N = int(input())  # 첫 줄: 수의 개수
numbers = list(map(int, input().split()))  # 다음 줄: N개의 수
# 소수 개수 계산 및 출력
print(count_primes(numbers))

#https://www.acmicpc.net/problem/2231 문제
def find_smallest_generator(N):
    start = max(1, N - len(str(N)) * 9)  # 탐색 시작 지점 최적화
    for i in range(start, N):
        if i + sum(map(int, str(i))) == N:
            return i
    return 0
N = int(input())
print(find_smallest_generator(N))

#https://www.acmicpc.net/problem/2292 문제
import math
def min_rooms_to_pass(N):
    if N == 1:
        return 1  # 시작점이 목적지인 경우
    # N이 속한 층 계산하기
    # 각 층의 마지막 방 번호: 1, 7, 19, 37, 61... 은 1 + 3n(n+1) 패턴
    # 3n² + 3n + 1 - N ≥ 0 방정식 풀기
    n = (-3 + math.sqrt(9 + 12 * (N - 1))) / 6
    layer = math.ceil(n)  # 올림
    return layer + 1  # 시작과 끝 방 포함
# 입력 받기
N = int(input())
# 결과 출력
print(min_rooms_to_pass(N))

#https://www.acmicpc.net/problem/2798 문제
import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
max_sum = 0
for combo in combinations(cards, 3):
    current = sum(combo)
    if current <= m and current > max_sum:
        max_sum = current
print(max_sum)

#https://www.acmicpc.net/problem/15829 문제
import sys
L = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
M = 1234567891
hash_value = 0
for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1
    hash_value += char_value * (31 ** i)
print(hash_value % M)

#https://www.acmicpc.net/problem/1259 문제
import sys
while True:
    num = sys.stdin.readline().strip()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')

#https://www.acmicpc.net/problem/1546 문제
n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
new_scores = [(score/m)*100 for score in scores]
print(sum(new_scores)/n)

#https://www.acmicpc.net/problem/2609 문제
import math
a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = (a * b) // gcd
print(gcd)
print(lcm)

#https://www.acmicpc.net/problem/2775 문제
# DP 테이블 초기화 (15x15)
apartment = [[0] * 15 for _ in range(15)]
# 0층 초기화 (0층 i호 = i명)
for i in range(1, 15):
    apartment[0][i] = i
# 모든 층의 1호는 1명
for floor in range(1, 15):
    apartment[floor][1] = 1
# DP 테이블 채우기
for floor in range(1, 15):
    for room in range(2, 15):
        apartment[floor][room] = apartment[floor][room-1] + apartment[floor-1][room]
# 테스트 케이스 처리
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apartment[k][n])

#https://www.acmicpc.net/problem/2869 문제
import math
A, B, V = map(int, input().split())
if V <= A:
    print(1)
else:
    effective_climb = A - B
    days = math.ceil((V - A) / effective_climb) + 1
    print(days)

#https://www.acmicpc.net/problem/10989 문제
import sys
n = int(sys.stdin.readline())
count = [0] * 10001  # 수의 범위가 1~10000이므로 10001 크기의 배열 생성
# 각 수의 등장 횟수 계산
for _ in range(n):
    count[int(sys.stdin.readline())] += 1
# 결과 출력
for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)

#https://www.acmicpc.net/problem/11050 문제
n, k = map(int, input().split())
if k < 0 or k > n:
    print(0)
else:
    k = min(k, n - k)
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i
    print(result)

#https://www.acmicpc.net/problem/28702 문제
# 세 개의 문자열을 입력으로 받음
strings = [input() for _ in range(3)]
# 입력된 문자열 중 숫자를 찾아 다음 문자열 결정
for i in range(3):
    if strings[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        # 다음 값은 현재 숫자 + (3 - 현재 위치)
        next_value = int(strings[i]) + (3 - i)
        # FizzBuzz 규칙에 따라 다음 문자열 결정
        if next_value % 3 == 0 and next_value % 5 == 0:
            print("FizzBuzz")
        elif next_value % 3 == 0:
            print("Fizz")
        elif next_value % 5 == 0:
            print("Buzz")
        else:
            print(next_value)
        # 결과를 찾았으므로 루프 종료
        break