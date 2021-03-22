string = str(input())
flag = "normal"
temp = ""

for i in range(len(string)):
    if string[i] == '<' or flag == "open":
        flag = "open"
        if temp:
            print(temp[::-1], end='')
            temp = ""
            temp += string[i]
        else:
            temp += string[i]
            continue
    if string[i] == '>':
        temp += string[i]
        print(temp, end='')
        temp = ""
        flag = "normal"
    if string[i] == " " and flag == "normal":
        print(temp[::-1], end='')
        print(" ", end='')
        temp = ""
    else:
        temp += string[i]

    i += 1

print(temp[::-1], end='')
