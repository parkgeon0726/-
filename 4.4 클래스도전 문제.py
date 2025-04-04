#4.4 클래스도전 관련5문제

#https://www.acmicpc.net/problem/11723 문제
import sys
def main():
    s = 0
    output = bytearray()
    M = int(sys.stdin.readline())
    for _ in range(M):
        line = sys.stdin.readline().rstrip()  # rstrip()이 strip()보다 처리 속도 빠름
        cmd, _, x_str = line.partition(' ')
        if cmd in ('add', 'remove', 'check', 'toggle'):
            x = int(x_str) - 1
            mask = 1 << x
            if cmd == 'add':
                s |= mask
            elif cmd == 'remove':
                s &= ~mask
            elif cmd == 'check':
                output.extend(b'1\n' if (s & mask) else b'0\n')  # 바이트 연산으로 메모리 최적화
            elif cmd == 'toggle':
                s ^= mask
        elif cmd == 'all':
            s = (1 << 20) - 1  # 0b11111111111111111111
        elif cmd == 'empty':
            s = 0
    sys.stdout.buffer.write(output)  # 버퍼 직접 출력으로 I/O 최적화
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/1620 문제
import sys
# 입력 처리 최적화
input = sys.stdin.readline
# N개의 포켓몬, M개의 질문
N, M = map(int, input().split())
# 하나의 딕셔너리에 두 가지 매핑 저장
pokemon_dict = {}
# N개의 포켓몬 정보 입력
for i in range(1, N + 1):
    name = input().strip()
    pokemon_dict[i] = name
    pokemon_dict[name] = i
# M개의 질문에 대한 응답
for _ in range(M):
    query = input().strip()
    # 숫자인 경우 포켓몬 이름 출력
    if query.isdigit():
        print(pokemon_dict[int(query)])
    # 문자인 경우 포켓몬 번호 출력
    else:
        print(pokemon_dict[query])

#https://www.acmicpc.net/problem/1764 문제
import sys
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    heard = set(input().strip() for _ in range(N))
    seen = set(input().strip() for _ in range(M))
    intersection = heard & seen
    print(len(intersection))
    for name in sorted(intersection):
        print(name)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/11047 문제
import sys
def main():
    # 입력 처리 최적화
    input = sys.stdin.readline
    N, K = map(int, input().split())
    # 동전 리스트 생성 (오름차순 입력)
    coins = [int(input().strip()) for _ in range(N)]
    # 그리디 알고리즘 수행
    count = 0
    for coin in reversed(coins):  # 내림차순 순회
        if K == 0:
            break
        if coin > K:
            continue
        # 현재 동전으로 만들 수 있는 최대 개수 계산
        count += K // coin
        K %= coin  # 남은 금액 업데이트
    print(count)
if __name__ == "__main__":
    main()

#https://www.acmicpc.net/problem/11399 문제
import sys
def main():
    # 입력 처리 최적화
    input = sys.stdin.readline
    N = int(input())
    times = list(map(int, input().split()))
    # 처리 시간 오름차순 정렬
    times.sort()
    total_time = 0
    current_sum = 0
    for time in times:
        current_sum += time
        total_time += current_sum
    print(total_time)
if __name__ == "__main__":
    main()