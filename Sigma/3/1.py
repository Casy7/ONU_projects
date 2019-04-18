from random import randint
inp1=tuple([randint(0,5) for i in range(10)])
inp2=tuple([randint(-5,0) for i in range(10)])
inp3=tuple(inp1+inp2)
print(inp3.count(0))
print(inp3)