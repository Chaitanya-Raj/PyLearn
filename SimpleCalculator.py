import os

print("Welcome to Simple Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Exponentiation")
choice = int(input("Choose an option : "))
print()
x = float(input("Enter the first number : "))
y = float(input("Enter the second number : "))

if choice == 1:
    result = x + y
if choice == 2:
    result = x - y
if choice == 3:
    result = x * y
if choice == 4:
    result = x / y
if choice == 5:
    result = x % y
if choice == 6:
    result = x ** y

print()
print("The result of the operation is "+str(result))

os.system("pause")