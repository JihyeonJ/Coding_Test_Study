s = str(input())

cnt = 0
for i in range(len(s)-1):
    if s[i] == ' ':
        cnt += 1
print(cnt+1)