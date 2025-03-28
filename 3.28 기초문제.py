#3.28 빠른입출력과 배열 관련문제풀이 (새싹문제풀이임)

#https://www.acmicpc.net/problem/15552 문제
#import sys
#def main():
    # 입력을 빠르게 받기 위해 sys.stdin.readline 사용
#    input = sys.stdin.readline
#    output = sys.stdout.write
    # 첫 줄에 테스트케이스 개수 T 입력받기
#    T = int(input().strip())
    # 결과를 저장할 리스트 초기화
#    results = []
    # T번 반복하며 두 정수 A와 B 입력받고 합 계산
#    for _ in range(T):
#        A, B = map(int, input().strip().split())
#        results.append(A + B)
    # 결과를 한 번에 출력 (빠르게 출력하기 위해 sys.stdout.write 사용)
#    output('\n'.join(map(str, results)) + '\n')
#if __name__ == "__main__":
#    main()

#https://www.acmicpc.net/problem/10871 문제
# 첫째 줄 입력: N과 X
#N, X = map(int, input().split())
# 둘째 줄 입력: 수열 A
#A = list(map(int, input().split()))
# X보다 작은 수를 필터링하여 출력
#result = [str(num) for num in A if num < X]
#print(" ".join(result))

#https://www.acmicpc.net/problem/10807 문제
# 첫째 줄 입력: 정수의 개수 N
#N = int(input())
# 둘째 줄 입력: N개의 정수
#numbers = list(map(int, input().split()))
# 셋째 줄 입력: 찾으려는 정수 v
#v = int(input())
# v의 개수를 세어 출력
#count = numbers.count(v)
#print(count)

#https://www.acmicpc.net/problem/5597 문제
# 모든 학생의 출석번호 (1번부터 30번까지)
#all_students = set(range(1, 31))
# 과제를 제출한 학생들의 출석번호 입력받기
#submitted_students = {int(input()) for _ in range(28)}
# 제출하지 않은 학생의 출석번호 찾기
#missing_students = sorted(all_students - submitted_students)
# 결과 출력
#print(missing_students[0])
#print(missing_students[1])

#https://www.acmicpc.net/problem/2738 문제
# 첫째 줄 입력: 행렬의 크기 N과 M
#N, M = map(int, input().split())
# 행렬 A 입력받기
#A = [list(map(int, input().split())) for _ in range(N)]
# 행렬 B 입력받기
#B = [list(map(int, input().split())) for _ in range(N)]
# 두 행렬을 더한 결과 계산
#result = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]
# 결과 출력
#for row in result:
#    print(" ".join(map(str, row)))