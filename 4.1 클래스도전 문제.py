#4.1 클래스도전 관련문제

#https://www.acmicpc.net/problem/2439 문제
# 입력 받기
N = int(input())
# 별 출력
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)

#https://www.acmicpc.net/problem/11720 문제
# 입력 받기
N = int(input())  # 숫자의 개수 입력
numbers = input()  # 공백 없이 쓰여 있는 숫자들 입력
# 숫자 합 계산
total = sum(int(num) for num in numbers)
# 결과 출력
print(total)

#https://www.acmicpc.net/problem/31403 문제
# 입력 받기
A = int(input())  # 첫 번째 정수 입력
B = int(input())  # 두 번째 정수 입력
C = int(input())  # 세 번째 정수 입력
# 숫자로 계산
result_integer = A + B - C
# 문자열로 계산
A_str = str(A)
B_str = str(B)
C_str = str(C)
result_string_concat = A_str + B_str  # 문자열 이어붙이기
result_string_subtraction = int(result_string_concat) - int(C_str)  # 문자열을 숫자로 변환 후 빼기
# 결과 출력
print(result_integer)  # 숫자로 계산한 결과
print(result_string_subtraction)  # 문자열로 계산한 결과

#https://www.acmicpc.net/problem/2562 문제
# 9개의 숫자 입력 받기
numbers = [int(input()) for _ in range(9)]
# 최댓값과 인덱스 찾기
max_value = max(numbers)
position = numbers.index(max_value) + 1  # 1부터 시작하는 위치 계산
# 결과 출력
print(max_value)
print(position)

#https://www.acmicpc.net/problem/2884 문제
H, M = map(int, input().split())
# 45분 빼기
M -= 45
if M < 0:  # 분이 음수가 되면 시간 조정
    M += 60
    H -= 1
    if H < 0:  # 시간이 음수가 되면 23시로 보정
        H = 23
print(H, M)

#https://www.acmicpc.net/problem/10250 문제
# 테스트 케이스 수 입력
T = int(input())
for _ in range(T):
    # 호텔 정보 및 손님 번호 입력 (H: 층수, W: 각 층의 방 수, N: 손님 번호)
    H, W, N = map(int, input().split())
    # 층수 계산 (N % H)
    floor = N % H
    if floor == 0:  # N이 H의 배수인 경우 꼭대기 층
        floor = H
    # 호수 계산 (N을 H로 나눈 몫 + 1)
    room = N // H + 1
    if N % H == 0:  # N이 H의 배수인 경우 몫만 사용
        room = N // H
    # 방 번호 출력 (층수 × 100 + 호수)
    print(floor * 100 + room)

#https://www.acmicpc.net/problem/10818 문제
# 입력 받기
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])  # 첫 번째 줄: 정수의 개수
numbers = list(map(int, data[1:]))  # 두 번째 줄: N개의 정수
# 최솟값과 최댓값 계산
min_value = min(numbers)
max_value = max(numbers)
# 결과 출력
print(min_value, max_value)

#https://www.acmicpc.net/problem/1152 문제
# 문자열 입력 받기
text = input()
# 문자열을 공백으로 분할하고 단어 개수 세기
words = text.split()
count = len(words)
# 결과 출력
print(count)

#https://www.acmicpc.net/problem/2577 문제
from collections import Counter
A = int(input())
B = int(input())
C = int(input())
product = A * B * C
counter = Counter(str(product))
for i in range(10):
    print(counter.get(str(i), 0))

#https://www.acmicpc.net/problem/2675 문제
T = int(input())
for _ in range(T):
    R, S = input().split()
    result = ''.join([char * int(R) for char in S])
    print(result)

#https://www.acmicpc.net/problem/2920 문제
nums = list(map(int, input().split()))
ascending = nums == list(range(1, 9))
descending = nums == list(range(8, 0, -1))
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

#https://www.acmicpc.net/problem/3052 문제
remainders = set()
for _ in range(10):
    num = int(input())
    remainders.add(num % 42)
print(len(remainders))

#https://www.acmicpc.net/problem/8958 문제
T = int(input())
for _ in range(T):
    case = input().strip()
    score = current = 0
    for char in case:
        if char == 'O':
            current += 1
            score += current
        else:
            current = 0
    print(score)

#https://www.acmicpc.net/problem/10809 문제
S = input().strip()
result = ' '.join([str(S.find(chr(i))) for i in range(97, 123)])
print(result)