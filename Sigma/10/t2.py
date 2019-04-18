#date = input().split()
date_full = input()


def creat_diction_of_dates(dmy):
    m = [30, 31, 28]
    for i in range(3, 13):
        if(i % 2 == 0):
            m.append(30)
        else:
            m.append(31)
    mv = [m[0], 31]+m[2:]
    if(dmy[0] % 400 == 0 or (dmy[0] % 4 == 0 and dmy[0] % 100 != 0)):
        m = mv
    print(mv)
    diction = {}
    for i in range(1, 13):
        diction[i] = range(mv[i-1])
    i = 0
    # print(diction)
    #days = 0
    return diction


def is_date_right(date_full):
    dmy = date_full.split(".")
    for i in range(3):
        dmy[i] = int(dmy[i])
    diction = creat_diction_of_dates(dmy)
    if dmy[1] in diction and dmy[0] in diction[dmy[1]]:
        print("Дата верна:", date_full)
    else:
        print("Дата неверна")


is_date_right(date_full)
