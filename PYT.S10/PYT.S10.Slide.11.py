def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as detail:
    print(type(detail))
    print(f"Handling run-time error: {detail}")
