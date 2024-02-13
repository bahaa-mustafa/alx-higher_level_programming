#!/usr/bin/python3

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

print("--------")

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

print("--------")

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

print("---------")

a = [1, 2, 3, 4]
print(id(a))
a = a + [5]
print(id(a))

print("---------")

a = [1, 2, 3]
print(id (a))
a += [4]
print(id(a))
