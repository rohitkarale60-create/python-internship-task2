# Task 2: Control Flow & Logic Building

# 1. if-elif-else logic
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# 2. Nested loops (pattern)
print("\nPattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 3. Simple Calculator
print("\nCalculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operator")