data = (1,2,3), (4,5,6), (7,8,9), (10,11,12)
out1 = sum(data[0])
out2 = data[1][0]
out3 = 1
out4 = data[3][0]
for i in range(1,len(data[1])):
    out2-=data[1][i]
for i in range(len(data[2])):
    out3*=data[2][i]
for i in range(1,len(data[3])):
    out4/=data[3][i]
print(out1)
print(out2)
print(out3)
print(out4)