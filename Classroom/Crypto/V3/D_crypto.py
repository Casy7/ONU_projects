r2="8bg0dgdbg0dgfbg0dg3bg0dg7bg0dg#5bg0dg#bbg0dgdbg0dgbbg0dg38g1dg4bg0dg0bbg0dgdbg0dgbbg0dgaag0dg"

r2=r2[::-1]

r2 = r2.replace("g", " ")
r2 = r2.replace("#", "")

print(r2)

r = r2.decode("hex")
print(r)