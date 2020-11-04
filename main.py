#This calculates the average value of three numbers that are inputted by the user.
def calculate(a,b,c):
  answer = (a + b + c)/3
  print(f"The average value of these numbers is {answer}")

print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())
print("Enter the third number:")
num3 = int(input())

calculate(num1,num2,num3)