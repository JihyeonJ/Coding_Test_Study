# N: 숫자 배열의 길이
# M: 더할 횟수
# K: 연속 가능한 횟수
N, M, K = map(int, input().split())
res = 0; 

# data는 숫자 배열
data = list(map(int, input().split()))
data.sort(reverse=True);

while(True):
    if (M - K >= 0):
        res += (K * data[0]); 
        M -= K;
    if (M - 1 >= 0):
        res += data[1];
        M -= 1;
    if (M == 0):
        break;

print(res)