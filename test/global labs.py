dataset = """ID, NAME, BALANCE, FEES, TYPE
12, Luanne Jaynie Brooke, 9552.4, False, 1
10, Shari Antonia Penders, 5548.15, False, 1
24, Raffael Cole Read, 9375.64, False, 2
62, Bishop Arno Ware, 2166.48, True, 3
18, Gladwin Isador Shearer, 2398.2, True, 1
65, Marilou Marcy Lawrenz, 5821.93, False, 2
10, Susi Joy Fischer, 2280.66, True, 2
38, Louise McKinley Bean, 8370.33, False, 3
52, Clara Theofilus Van Houten, 7637.84, False, 4
61, Puck Rain Reuter, 3012.5, True, 1
75, Hilma Lindy Teel, 9125.07, False, 1
42, Deforest Arno Jeffery, 7914.34, False, 4
17, Hattie Ariana Seward, 4672.84, True, 3
92, Maurine Tineke Maurer, 3792.1, True, 3
34, Trey Allegra Brooke, 4108.71, True, 1
16, Tatum Reimund Van den Andel, 8911.06, False, 2
89, Beaumont Lena Hanson, 1372.97, True, 1
35, Pim Jerrod Klerken, 6462.17, False, 4
88, Emmett Jordon Krämer, 4774.42, True, 2
23, Jennie Alexandria Fischer, 7771.9, False, 4"""


def A(input_dataset):
    res = []

    first_split = input_dataset.split('\n')
    for line in first_split:
        res.append(line.split(", "))

    return res


def B(table, target_idx):
    res_name = set()

    if target_idx <= 0 or target_idx > len(table[0]):
        return False

    target_idx -= 1
    for i in range(1, len(table)):
        if isinstance(table[i][target_idx], str) == False:
            continue
        for j in table[i][target_idx]:
            res_name.add(j)

    return len(res_name)


def C(table, target_idx):
    if target_idx <= 0 or target_idx > len(table[0]):
        return False

    target_idx -= 1
    total = 0
    res1, res2, res3 = 0, 0, 0

    for i in range(1, len(table)):
        try:
            total += float(table[i][target_idx])
        except:
            print("not numeric")
    res1 = round(total, 0)
    res2 = round(total/(len(table)-1), 0)

    total = 0
    for i in range(1, len(table)):
        try:
            total += (float(table[i][target_idx]) - res2)**2
        except:
            print("not numeric")
    res3 = round((total/(len(table)-1))**(1/2), 2)

    res_t = (res1, res2, res3)

    return res_t


def D(table, target_idx):
    if target_idx <= 0 or target_idx > len(table[0]):
        return False

    res_set = set()
    target_idx -= 1
    for i in range(1, len(table)):
        if table[i][target_idx].isdigit() == False:
            continue
        res_set.add(table[i][target_idx])

    return len(res_set)


def E(table, new_list):
    if len(new_list) != len(table[0]):
        return False

    if str(type(new_list[0])) != "<class 'int'>":
        print("wrong ID")
        return False
    if str(type(new_list[1])) != "<class 'str'>":
        print("wrong NAME")
        return False
    if str(type(new_list[2])) != "<class 'float'>":
        print("wrong BALANCE")
        return False
    if str(type(new_list[3])) != "<class 'str'>":
        print("wrong FEES")
        return False
    if str(type(new_list[4])) != "<class 'int'>":
        print("wrong TYPE")
        return False

    table.append(new_list)
    return table


def F(table, del_idx):
    for i in range(len(del_idx)):
        print(del_idx[i])
        # Validate that the record indexes are in range
        if del_idx[i] <= 0 or del_idx[i] > len(table):
            continue
        else:
            del table[del_idx[i]]      # Remove record from the table

    return table


A_res = A(dataset)
B(A_res, 2)
C(A_res, 3)
print(D(A_res, 5))
E(A_res, [10, 'Katie', 1011.43, 'TRUE', 2])
F(A_res, [20, 21])
