arr = str(input());
tmp = 0;
res = 1;

for i in arr:
    tmp = int(i); 
    if tmp == 0:
        res += tmp; 
    else:
        res *= tmp;  
        
print(res);