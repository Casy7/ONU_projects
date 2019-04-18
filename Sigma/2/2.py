ipnut_str = []
input_int = int(input())
di = {}
for i in range(input_int):
	ipnut_str.extend(input().split())
ipnut_str.sort()
for i in range(len(ipnut_str)):
	if ipnut_str[i] in di.keys():
		di[ipnut_str[i]] += 1
	else:
		di[ipnut_str[i]] = 1
highest_value=max(di.values())
to_final_find=list(di.items())
for i in range (len(to_final_find)):
	list(to_final_find[i])
	if to_final_find[i][1]==highest_value:
		number = to_final_find[i][0]
		break
print(number)