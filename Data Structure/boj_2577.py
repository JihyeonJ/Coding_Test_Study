A = int(input())
B = int(input())
C = int(input())

res = str(A*B*C)
chk = [0 for i in range(0, 10)]

for i in res:
    if i == "0":
        chk[0] += 1
    elif i == "1":
        chk[1] += 1
    elif i == "2":
        chk[2] += 1
    elif i == "3":
        chk[3] += 1
    elif i == "4":
        chk[4] += 1
    elif i == "5":
        chk[5] += 1
    elif i == "6":
        chk[6] += 1
    elif i == "7":
        chk[7] += 1
    elif i == "8":
        chk[8] += 1
    elif i == "9":
        chk[9] += 1        
        

for i in chk:
    print(i)