test1="Berlin"
test="67"
def f1():
    def f2():
        def f3():
            test="New York"
            nonlocal test
            print(test)
        f3()
        print(test)
    f2()
    print(test)
f1()
print(test)