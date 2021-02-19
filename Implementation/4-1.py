N = int(input());
move = list(map(str, input().split()));
x = 1;
y = 1;

for i in move:
    if i == "R" and (x+1) <= N:
        x += 1;        
    elif i == "L" and (x-1) > 0:
        x -= 1;
    elif i == "U" and (y-1) > 0:
        y -= 1;
    elif i == "D" and (y+1) <= N:
        y += 1;

print(y, x);