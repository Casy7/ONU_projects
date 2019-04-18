

inp = open("D:\\INPUT.txt")
all_inp = inp.read().split()
for i in range(6):
    all_inp[i]=int(all_inp[i])
print(all_inp)
(x_a,y_a) = (all_inp[4],all_inp[5])
x1,y1,x2,y2 = all_inp[:4]
result = []
if y1 == y2:
	is_axis_ox = True
	result = [x_a,2*y1-y_a]
else:
	is_axis_ox = False
	result = [2*x1-x_a,y_a]
print(result)
otp = open("D:\\OUTPUT.txt","w")
otp.write(str(result[0])+" "+str(result[1]))
otp.close()