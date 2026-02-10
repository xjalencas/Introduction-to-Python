try:
    f = open("myfile.txt", "r")
    s = f.readline()
    i = int(s.strip())

except IOError as e:
    print("I/O error (%s): %s" % (e.errno, e.strerror))

except ValueError:
    print("Could not convert data to an integer.")

except Exception:
    print("Unexpected error")
    raise
