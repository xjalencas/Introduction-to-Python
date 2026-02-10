import sys


def divide(x, y):

    try:
        result = x/y

    except ZeroDivisionError:
        sys.stderr.write("Dividing by 0. Returning infinite\n")
        result = float("Inf")

    else:
        print(f"Result is {result}")

    finally:
        print("Executing finally clause")

    return result


print(divide(1, "0"))
