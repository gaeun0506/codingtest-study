import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

arr = [list(map(int, input().strip())) for _ in range(1)]

arr2 = arr[0]

arr2.sort(reverse=True)

print(*arr2, sep='')