# N: 숫자 배열의 길이
# M: 더할 횟수
# K: 연속 가능한 횟수
N, M, K = map(int, input().split())
res = 0; 

# data는 숫자 배열
data = list(map(int, input().split()))
data.sort(reverse=True);

first = (M / (K + 1)) * K;
second = (M / (K + 1));

res = (first * data[0]) + (second * data[1]);
print(int(res));