#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg == 1:
        print("0 arguments.")

    else:
        if arg == 2:
            print("{} argument:".format(arg - 1))

        else:
            print("{} arguments:".format(arg - 1))

        for i in range(arg - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
