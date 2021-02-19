input_arr = list(input());
sort_arr = sorted(input_arr);

alpha_arr = "";
num_arr = "";
for i in range(0, len(sort_arr)):
    if sort_arr[i].isalpha() == True:
        alpha_arr += str(sort_arr[i]);
    else:
        num_arr += str(sort_arr[i]);

print(alpha_arr+num_arr);