#!/usr/bin/python3
"""function module."""


def add_integer(a, b=98):
	"""add function.

	Args:
		a: frist number integer or float
		b: second number integer or float

	Raise:
		TypeError: if a and b not integer or float

	Return:
		add of a and b
	"""

	try:
		a = a - 0
	except:
		print("a must be an integer")
	try:
		b = b - 0
	except:
		print("b must be an integer")
	a = int(a)
	b = int(b)
	return a + b
