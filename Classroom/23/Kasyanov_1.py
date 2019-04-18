fst_file = input()
snd_file = input()
with open (fst_file,"r",encoding = "UTF-8") as file1:
	with open (snd_file,"r",encoding = "UTF-8") as file2:
		arr1=[]
		arr2=[]
		for line in file1:
			arr1.append(line)
		for line in file2:
			arr2.append(line)
differents = False
for i in range(len(arr1)):
	if arr1[i] != arr2[i]:
		print(arr1[i]+arr2[i])
		differents = True
if differents == False:
	print("Строки совпали")
	



