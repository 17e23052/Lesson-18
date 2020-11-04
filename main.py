#This multiplies two numbers that are inputted by the user.
def calculate(a,b):
  answer = a * b
  print(f"{a} * {b} = {answer}")

print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())

calculate(num1,num2)