N = int(input());
arr = list(map(int, input().split()));
res = 0;

arr.sort();

for i in arr:
    if (N - i <= 0):
        break;
    N -= i;
    res += 1

print(res);