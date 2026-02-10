def function3():
    print("I am executing function 3")
    return 1/0


def function2():
    print("I am executing function 2")
    try:
        return function3()
    except ZeroDivisionError:
        print("Trying to divide by 0!")
        return


def function1():
    print("I am executing function 1")
    return function2()


print(function1())
