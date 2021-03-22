import sys

N = int(input())
M = int(input())
friend = dict()

for i in range(1, N+1):
    friend[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

ans_set = set(friend[1])
print(ans_set)
