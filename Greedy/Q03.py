arr = str(input()); 
save = arr[0];
cnt = 0;

for i in range(1, len(arr)):
    if arr[i] == save:
        continue;
    else:
        if save == 0:
            save = 1;
        else:
            save = 0;
        cnt += 1;

print(cnt)



10001100 -> 2
00001100 -> 1
00100110 -> 