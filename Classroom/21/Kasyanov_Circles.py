inp = open("D:\\INPUT.txt")
all_inp = inp.read().split()
for i in range(6):
    all_inp[i]=int(all_inp[i])
input_w1 = all_inp[:3]
input_w2 = all_inp[3:6]
(x1,y1,r1)=input_w1
(x2,y2,r2)=input_w2
result = "NO"
if ((x1-x2)**2+(y1-y2)**2)**0.5<=r1+r2:
	result = "YES"
print(result)
otp = open("D:\\OUTPUT.txt","w")
otp.write(result)
otp.close()
