
try:
    fd = open("myfile.txt", "r")
    x = 10 / 0

finally:
    print(fd.closed)
    print("Closing opened files")
    fd.close()
