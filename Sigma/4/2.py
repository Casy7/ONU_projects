total = 0  # variable


def sum(arg1, arg2):
    total = arg1 + arg2
    #
    print("Inside the function local total : ", total)
    return [total, arg1, arg2, "Print"]


# Now you can call sum function what if assign
print(sum(10, 20))
print("Outside the function global total : ", total)
