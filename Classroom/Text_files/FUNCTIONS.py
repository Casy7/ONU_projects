def printarray(c=[]):
    for x in range(len(c)):
        for i in range(len(c[0])):
            print("{:4d}".format(c[x][i]), end="")
        print("")


def create(m=0, n="Err", r=9):
    if(n == "Err"):
        n = m
    g = []
    if r == 0:
        for i in range(m):
            m1 = []
            for j in range(n):
                m1.append(0)
            g.append(m1)
    else:
        from random import randint
        for i in range(m):
            m1 = []
            for j in range(n):
                m1.append(randint(0, r))
            g.append(m1)
    return g

def create_matrix():
	return 0


def arrtodigit(a=[]):
    for i in range(len(a)):
        a[i] = float(a[i])
        if a[i] % 1 == 0:
            a[i] = int(a[i])
    return a


printarray(create(3, 5))
# m=int(input("Введите длину массива:  "))
# n=int(input("Введите ширину массива:  "))
# print(arrtodigit(create(3,4,23)))
create_matrix("""
#********
*@####*#*
*#*****#*




""")