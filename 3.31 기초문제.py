#3.31 문자열과 함수 관련문제풀이 (새싹문제풀이임)

#https://www.acmicpc.net/problem/11654 문제
# 입력받은 문자
char = input()
# 아스키 코드 값 출력
print(ord(char))

#https://www.acmicpc.net/problem/2743 문제
# 단어 입력받기
word = input()
# 단어의 길이 출력
print(len(word))

#https://www.acmicpc.net/problem/2744 문제
# 단어 입력받기
word = input()
# 대문자는 소문자로, 소문자는 대문자로 변환
converted_word = word.swapcase()
# 변환된 단어 출력
print(converted_word)

#https://www.acmicpc.net/problem/2754 문제
# 성적 입력받기
grade = input()
# 성적에 따른 평점 딕셔너리
grade_to_gpa = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0 }
# 평점 출력
print(grade_to_gpa[grade])

#https://www.acmicpc.net/problem/27866 문제
# 단어 S 입력받기
S = input()
# 정수 i 입력받기
i = int(input())
# i번째 글자 출력 (1부터 시작하므로 인덱스는 i-1)
print(S[i - 1])

#https://www.acmicpc.net/problem/11718 문제
import sys
# 입력받은 내용을 한 줄씩 읽어서 출력
for line in sys.stdin:
    print(line.rstrip())

#https://www.acmicpc.net/problem/9086 문제
# 테스트 케이스 개수 입력받기
T = int(input())
# 각 테스트 케이스 처리
for _ in range(T):
    string = input()
    # 첫 글자와 마지막 글자를 연속하여 출력
    print(string[0] + string[-1])

#https://www.acmicpc.net/problem/15964 문제
a, b = map(int, input().split())
print((a + b) * (a - b))

#https://www.acmicpc.net/problem/2475 문제
# 5개의 숫자를 입력받기
numbers = list(map(int, input().split()))
# 각 숫자를 제곱한 후 합산
sum_of_squares = sum(num ** 2 for num in numbers)
# 검증수 계산
verification_number = sum_of_squares % 10
# 검증수 출력
print(verification_number)