exin = str(input())
croc = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0

for i in croc: 
    cnt += exin.count(i)

print(cnt + (len(exin) - cnt*2))