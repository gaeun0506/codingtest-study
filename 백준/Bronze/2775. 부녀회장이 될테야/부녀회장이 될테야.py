import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

for i in range(t):
    #k층 n호
    k = int(input())
    n = int(input())

    f0 = [x for x in range(1, n + 1)]  # 0층 리스트
    for k in range(k):  # 층 수 만큼 반복
        for i in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i - 1]  # 층별 각 호실의 사람 수를 변경

    print(f0[-1])  # 가장 마지막 수 출력