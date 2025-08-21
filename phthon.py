import sys

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error! Division by zero." if b==0 else a/b

if len(sys.argv) != 4:
    print("Usage: python phthon.py <choice> <num1> <num2>")
    print("Choice: 1=Add, 2=Subtract, 3=Multiply, 4=Divide")
    sys.exit(1)

choice = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if choice == '1': print(add(num1, num2))
elif choice == '2': print(subtract(num1, num2))
elif choice == '3': print(multiply(num1, num2))
elif choice == '4': print(divide(num1, num2))
else: print("Invalid choice")
