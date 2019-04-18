side_len=float(input("Введите длину стороны: "))
Perim=4*side_len
Square=side_len**2
Diagonal=round(side_len*2**0.5,2)
output = Perim, Square, Diagonal
print("P,S,d: ",*output)