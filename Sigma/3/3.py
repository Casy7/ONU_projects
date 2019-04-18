import operator
tur=tuple("Dima,19,180 Nastya,20,190 Kolya,17,191 Natasha,13,193 Lera,21,185".split(" "))
tup1=[]
for i in range(len(list(tur))):
    timelist=tur[i].split(",")
    tup=timelist[0],int(timelist[1]),int(timelist[2])
    tup1.append(tup)
print(tup1)

maxhigh=max(tup1, key=operator.itemgetter(0))
minhigh=min(tup1, key=operator.itemgetter(0))
maxage=max(tup1, key=operator.itemgetter(1))
minage=min(tup1, key=operator.itemgetter(1))
print("The youngest:",minage[0],"\n","The oldest:",maxage[0],"\n","The lowest:",minhigh[0],"\n","The tallest:",maxhigh[0])
