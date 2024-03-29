#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        print("Inside result: {}".format(a / b))
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        return ((a / b) if b != 0 else None)
