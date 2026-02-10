def function3():
    print("I am executing function 3")
    return 1/0


def function2():
    print("I am executing function 2")
    return function3()


def function1():
    print("I am executing function 1")
    return function2()


function1()
