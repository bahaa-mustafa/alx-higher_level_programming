#!/usr/bin/python3
def remove_char_at(str, n):
    copyStr = ""
    for i in range(len(str)):
        if i == n:
            continue
        copyStr = copyStr + str[i]
    return copyStr
