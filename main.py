#This finds the highest number out of two numbers that are inputted by the user.
def calculate(a,b):
  if a == b:
    print("The numbers are the same")
  elif a > b:
    highest_num = a
  elif b > a:
    highest_num = b
  if a > b or b > a:
    print(f"The highest number entered is {highest_num}")

print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())

calculate(num1,num2)