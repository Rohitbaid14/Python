def circle():
    radius = int(input("Enter the radius of the circle :"))
    area = 3.14*radius*radius
    print("The area of circle is :",area)
    
def rectangle():
    l = int(input("Enter the length of the rectangle :"))
    w = int(input("Enter the width of the rectangle :"))
    area = l * w
    print("The area of rectangle is :",area)
    
def triangle():
    h = int(input("Enter the height of the triangle :"))
    b = int(input("Enter the base of the triangle :"))
    area = 0.5 * h * b
    print("The area of triangle is :",area)

while(1):
    print("\n\n\t\t\t\tArea Calculator\t\t\t\n\n")
    print("1.Area of a rectancle")
    print("2.Area of a circle")
    print("3.Area of a triangle")
    print("4. Exit")
    choice = int(input("Enter your choice :"))

    if (choice == 1):
      rectangle()

    elif (choice == 2):
      circle()

    elif (choice == 3):
      triangle()

    elif (choice == 4):
       print("Thank you!")
       break
    
    else:
      print("\nInvalid option!!! Try again\n\n")