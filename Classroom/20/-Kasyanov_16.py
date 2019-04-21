'''Лабиринт представляет собой квадрат, состоящий из NxN сегментов. Каждый из сегментов может быть либо пустым, 
либо заполненным монолитной каменной стеной. Гарантируется, что левый верхний и правый нижний сегменты пусты. 
Лабиринт обнесён сверху, снизу, слева и справа стенами, оставляющими свободными только левый верхний и правый 
нижний углы. Директор лабиринта решил покрасить стены лабиринта, видимые изнутри (см. рисунок). Помогите ему 
рассчитать количество краски, необходимой для этого.'''
w=[[0,0,0,0,0],[0,0,0,1,1],[0,0,1,0,0],[0,0,1,1,1],[0,0,0,0,0]]

c=0
x=0
y=1
for i in range(1,len(w)-1):
	j=0
	for i in range(1,len(w[0])-2):
		if(w[x][y]!=1 or w[x][y]!=None):		
			if(w[x-1][y]==1 or w[x-1][y]==None):
				w[x-1][y]=2
				#2 -- $
				#1 -- #
				c+=1
			if(w[x+1][y]==1 or w[x+1][y]==None):
				w[x+1][y]=2
				c+=1
			if(w[x][y-1]==1 or w[x][y-1]==None):
				w[x][y-1]=2
				c+=1
			if(w[x][y+1]==1 or w[x][y+1]==None):
				w[x][y+1]=2
				c+=1
			w[x][y]=0
		y=i
	y+=1
	x=0
print(c-4)


