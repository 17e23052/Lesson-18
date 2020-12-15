def add(a,b):
  add = a + b
  print(f"{a} + {b} = {add}")
def sub(a,b):
  sub = a - b
  print(f"{a} - {b} = {sub}")
def mul(a,b):
  mul = a * b
  print(f"{a} * {b} = {mul}")
def div(a,b):
  div = a / b
  print(f"{a} / {b} = {div}")

print("Enter a number:")
num1 = int(input())
print("Enter another number:")
num2 = int(input())
print("Enter +, -, * or /:")
print("If using divison, remainders will not be shown.")
operation = input()
if operation == "+":
  add(num1,num2)
elif operation == "-":
  sub(num1,num2)
elif operation == "*":
  mul(num1,num2)
elif operation == "/":
  div(num1,num2)
else:
  print("Invalid operation. Please start program")