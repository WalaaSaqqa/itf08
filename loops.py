def input_from_user():
   num1 = float(input("Enter the first number: "))
   num2 = float(input("Enter the second number: "))
   return num1, num2

def sum():
   num1 , num2 = input_from_user()
   sum = num1 + num2
   return sum

def subtract():
   num1 , num2 = input_from_user()
   sub = num1 - num2
   return sub

def multiply():
   num1 , num2 = input_from_user()
   mul = num1 * num2
   return mul

def divide():
   num1 , num2 = input_from_user()
   div = num1 / num2
   if num2 != 0:
      return div
   else:
      return "Cannot divide by zero."


def circle():
   radius = float(input("Enter the radius: "))
   area = (radius ** 2) * 3.14
   return  area

def triangle():
   base = float(input("Enter the base: "))
   height = float(input("Enter the height: "))
   area = 0.5 * base * height
   return area

def rectangle():
   length = float(input("Enter the length: "))
   width = float(input("Enter the width: "))
   area = length * width
   return area
def main():
   while True:
      print("Main Menu: ")
      print("1. Sum ")
      print("2. Subtract ")
      print("3. Multiply ")
      print("4. Division ")
      print("5. Calculate triangle area ")
      print("6. Calculate circle area ")
      print("7. Calculate rectangle area ")
      print("8. Exit ")

      select = input("Enter your selection:  ")

      if select == '1':
         print("Sum:", sum())
      elif select == '2':
         print("Sub:", subtract())
      elif select == '3':
         print("Mul:", multiply())
      elif select == '4':
         print("div:", divide())
      elif select == '5':
         print("Triangle Area:", triangle())
      elif select == '6':
         print("Circle Area:", circle())
      elif select == '7':
         print("Rectangle Area:", rectangle())
      elif select == '8':
         print("Exiting the program. Thank You ")
         break
      else:
         print("Invalid select. Try again and choose a valid option from 1 to 8 ")


main()
