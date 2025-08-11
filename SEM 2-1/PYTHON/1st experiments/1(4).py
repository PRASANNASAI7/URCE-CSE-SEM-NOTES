# i. Arithmetic operator:
a = 7
b = 2
print("Arithmetic Operators:")
print('sum:', a + b)
print('subtraction:', a - b)
print('multiplication:', a * b)
print('division:', a / b)
print('floor division:', a // b)
print('modulo:', a % b)
print('power:', a ** b)
print()  # Blank line for separation

# ii. Relational operator:
a = 5
b = 10
print("Relational Operators:")
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print()

# iii. Assignment operator:
a = 10
b = 5
a += b
print("Assignment Operator:")
print(a)
print()

# iv. Logical operator:
x = 10
y = 20
z = 30
m = (x > y) and (x < z)
n = (x > y) or (x < z)
p = not ((x > y) and (x < z))
q = not ((x < y) or (x < z))
print("Logical Operators:")
print(m)
print(n)
print(p)
print(q)
print()

# v. Bitwise Operator:
a = 10
b = 5
print("Bitwise Operators:")
print(a & b)
print(a | b)
print()

# vi. Ternary operator:
age = 15
result = 'yes' if age >= 18 else 'no'
print("Ternary Operator:")
print(result)
print()

# vii. Membership operator:
message = 'Hello world'
dict1 = {1: 'a', 2: 'b'}
print("Membership Operators:")
print('H' in message)
print('hello' not in message)
print(1 in dict1)
print()

# viii. Identity Operator:
x = 10
y = 10
a = "Hello"
b = "welcome"
print("Identity Operators:")
print(x is y)
print(a is not b)
