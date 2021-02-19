num = str(input()); 
left = num[:int(len(num) / 2)];
right = num[int(len(num) / 2):];

sum_left, sum_right = 0, 0;
for i in range(0, len(left)):
    sum_left += int(left[i]);
for i in range(0, len(right)):
    sum_right += int(right[i]);

if sum_left == sum_right:
    print("LUCKY");
else:
    print("READY");