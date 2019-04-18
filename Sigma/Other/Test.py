n = int(input())
lst = [1]*10 + [0]*(n // 2 * 9 - 9)
for i in range(n // 2 - 1):
	for it in range(len(lst)):	
		if it<10:
			lst[it]=sum(lst[:it+1])
		else:
			lst[it]=sum(lst[it-9:it+1])
'''res=0
for it in lst:
res += it**2'''
res = sum(it**2 for it in lst)
print(res)