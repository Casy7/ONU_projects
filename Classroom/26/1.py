n = int(input())
arr = input().split()
lenth = int(input())
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.append(0)
f = 0
for i in range(n):
    if arr[i] < lenth:
        print(i+1)
        f = 1
        break
        
if f == 0:
    print(n+1)
