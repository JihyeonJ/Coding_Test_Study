N = int(input());
inarr = list(map(int, input().split())); 
inarr.sort();
 
target = 1;
for x in inarr:
    if target < x:
        break;
    else:
        target += x;

print(target);