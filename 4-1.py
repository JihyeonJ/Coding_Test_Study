# N은 나눠질 수, M은 나눌 수
N, M = map(int, input().split());
count = 0;

while(N != 1):
    if (N % M == 0):
        N /= M;
    else:
        N -= 1;
    count += 1;

print(count);