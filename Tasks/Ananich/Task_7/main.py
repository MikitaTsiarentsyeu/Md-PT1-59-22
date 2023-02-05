import calc
# printing the starting line 
print("WELCOME TO A SIMPLE CALCULATION PROGRAM OF PERIMETERES AND AREAS OF VARIOUS SHAPES") 
# creating options 
while True: 
    print("\nMAIN MENU") 
    print("1. Calculate Perimeter") 
    print("2. Calculate Area") 
    print("3. Exit") 
    choice1 = int(input("Enter the Choice:")) 
 
    if choice1 == 1: 
        print("\nCALCULATE PERIMETER") 
        print("1. Circle") 
        print("2. Rectangle") 
        print("3. Square")
        print("4. Rhombus")
        print("5. Triangle") 
        print("6. Exit") 
        choice2 = int(input("Enter the Choice:")) 
 
        if choice2 == 1: 
            radius = int(input("Enter Radius of Circle:")) 
            calc.p_circle(radius) 
             
        elif choice2 == 2: 
            height = int(input("Enter Height of Rectangle:")) 
            width = int(input("Enter Width of Rectangle:")) 
            calc.p_rectangle(height, width) 
             
        elif choice2 == 3: 
            square_side = int(input("Enter Side of Square:")) 
            calc.p_square(square_side) 

        elif choice2 == 4: 
            rhombus_side = int(input("Enter Side of Rhombus:")) 
            calc.p_rhombus(rhombus_side)
        
        elif choice2 == 5: 
            side1 = int(input("Enter Side1 of Triangle:"))
            side2 = int(input("Enter Side2 of Triangle:"))
            side3 = int(input("Enter Side3 of Triangle:"))
            calc.p_triangle(side1, side2, side3)
 
        elif choice2 == 6: 
            break 
             
        else: 
            print("ERROR! Incorrect Choice.") 
     
    elif choice1 == 2: 
        print("\nCALCULATE AREA") 
        print("1. Circle") 
        print("2. Rectangle") 
        print("3. Square")
        print("4. Rhombus")
        print("5. Triangle") 
        print("6. Exit") 
        choice3 = int(input("Enter the Choice:")) 
 
        if choice3 == 1: 
            radius = int(input("Enter Radius of Circle:")) 
            calc.a_circle(radius) 
             
        elif choice3 == 2: 
            height = int(input("Enter Height of Rectangle:")) 
            width = int(input("Enter Width of Rectangle:")) 
            calc.a_rectangle(height, width) 
             
        elif choice3 == 3: 
            square_side = int(input("Enter Side of Square:")) 
            calc.a_square(square_side)

        elif choice3 == 4: 
            diagonal1 = int(input("Enter Diagonal1 of Rhombus:"))
            diagonal2 = int(input("Enter Diagonal2 of Rhombus:")) 
            calc.a_rhombus(diagonal1, diagonal2) 

        elif choice3 == 5: 
            side_triangle = int(input("Enter Side of Triangle:"))
            height_triangle = int(input("Enter Height of Triangle:")) 
            calc.a_triangle(side_triangle, height_triangle)

        elif choice3 == 6: 
            break 
             
        else: 
            print("ERROR! Incorrect Choice.") 
     
    elif choice1 == 3: 
        break 
     
    else: 
        print("ERROR! Incorrect Choice.") 
