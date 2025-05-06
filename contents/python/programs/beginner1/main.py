# IT IS RECOMENDED TO FULLY UNDERSTAND THE CONCEPT BEFORE GOING FOR PROGRAMS

# Program to input a value as float type and perform mathmateical operations on it.

num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

try:
  while True:
    print("Type: 1 for Addition, 2 for substraction(a - b), 3 for multiplication, 4 for division(a/b), 5 to quit")
    inp = int(input("> "))
    if inp == 1:
      sum = num1 + num2
      print(sum)
    elif inp == 2:
      sub = num1 - num2
      print(sub)
    elif inp == 3:
      prod = num1 * num2
      print(prod)
    elif inp == 4:
      div = num1 / num2
      print(div)
    elif inp == 5:
      print("Exiting program...")
      break
    else:
      print("Bad input")
except:
  print("Problem occured!")
