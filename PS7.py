from datetime import date

# Part-I: Find the Max of 3 Numbers
def max_3(num1, num2, num3):
  if num1 > num2:
    if num1 >= num3:
      return num1
    else:
      return num3
  elif num2 >= num1:
    if num2 > num3:
      return num2
    else:
      return num3
    if num1 >= num2 <= num3:
      return num1

print("\n>> Part-I\n")
num1 = int(input(" Enter 1st Number: "))
num2 = int(input(" Enter 2nd Number: "))
num3 = int(input(" Enter 3rd Number: "))
maximum = max_3(num1, num2, num3)
print("\n Max of Three:", maximum)
print()

# Part-II: Multiply all the Numbers in a list
print("\n>> Part-II\n")
def Mul_Of_List():
  list1 = []
  n = int(input(" Enter the Total Number of elements in desired list: "))
  for ele in range(n):
    ele = int(input("\n Enter the Element: "))
    list1.append(ele) 
  mul = 1
  for i in list1:
    mul = mul*i
  print("\n Multiplication of Elements in the list: ",mul)
Mul_Of_List()

# Part-III: Create a list of all Even Numbers between 19 & 88
print("\n\n>> Part-III\n")
def find_even(fro, to):
  even = []
  for i in range(fro, to + 1):
    if i % 2 == 0:
      even.append(i)
  return even

fro = int(input("From: "))
to = int(input("To: "))
even_res = find_even(fro, to)
print(even_res)
print()

# Part-IV: Display the current Date & Time & get the Python Version
print("\n>> Part-IV")
from datetime import date
import sys
print("\nDate:",date.today())
print("\nPython Version - ")
print (sys.version)
print("Version Info. - ")
print (sys.version_info)
