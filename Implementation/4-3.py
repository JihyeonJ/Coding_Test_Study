loc = str(input());
col = ord(loc[:1]) - 96; # a, b, c ...
row = int(loc[1:]);      # 1, 2, 3 ...

count = 0;
if (row+2) <= 8 and (col-1) >= 1:
    count += 1;
if (row+2) <= 8 and (col+1) <= 8:
    count += 1;    
if (row-2) >= 1 and (col-1) >= 1:
    count += 1;
if (row-2) >= 1 and (col+1) <= 8:
    count += 1; 
if (col+2) <= 8 and (row-1) >= 1:
    count += 1;
if (col+2) <= 8 and (row+1) <= 8:
    count += 1;    
if (col-2) >= 1 and (row-1) >= 1:
    count += 1;
if (col-2) >= 1 and (row+1) <= 8:
    count += 1; 

print(count);