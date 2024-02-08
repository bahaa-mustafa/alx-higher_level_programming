#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    result = 0
    if arg == 0:
        print(result)

    else:
        for i in range(1, arg + 1):
            result = result + int(sys.argv[i])

        print(result)
