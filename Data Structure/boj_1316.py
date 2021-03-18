N = int(input())
cnt = 0

for i in range(N):
    arr = []
    word = str(input())
    flag = 0

    for j in range(len(word)):
        if word[j] in arr:
            if word[j] == last:
                continue;
            flag = 1
            break;
        else:
            arr.append(word[j])
        last = word[j]
    
    if flag == 0:
        cnt += 1
print(cnt)