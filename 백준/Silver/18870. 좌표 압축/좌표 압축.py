import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')