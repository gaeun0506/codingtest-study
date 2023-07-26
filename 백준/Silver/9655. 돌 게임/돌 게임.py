import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

dp = [-1] * 10001
dp[1] = 1 #SK
dp[2] = 0 #CY
dp[3] = 1 #SK

for i in range(4, N + 1):
    if dp[i - 1] or dp[i - 3]: #dp[i - 1] == 1 or dp[i - 3] == 1
        dp[i] = 0
    else:
        dp[i] = 1
print('CY' if dp[N] == 0 else 'SK')