# defining functions

def p_circle(radius): 
    p = 2 * 3.14 * radius 
    print("Perimeter of Circle:", p) 
 
def p_rectangle(height, width): 
    p = 2 *(height + width) 
    print("Perimeter of Rectangle:", p) 
 
def p_square(square_side): 
    p = 4 * square_side 
    print("Perimeter of Square:", p) 

def p_rhombus(rhombus_side): 
    p = 4 * rhombus_side 
    print("Perimeter of Rhombus:", p)

def p_triangle(side1, side2, side3): 
    p = side1 + side2 + side3 
    print("Perimeter of Triangle:", p)

def a_circle(radius): 
    area = 3.14 * radius * radius 
    print("Area of Circle:", area) 
 
def a_rectangle(height, width): 
    area = height * width 
    print("Area of Rectangle:", area) 
 
def a_square(square_side): 
    area = square_side * square_side 
    print("Area of Square:", area)

def a_rhombus(diagonal1, diagonal2): 
    area = 0.5 * diagonal1 * diagonal2
    print("Area of Rhombus:", area)

def a_triangle(side_triangle, height_triangle): 
    area = 0.5 * side_triangle * height_triangle
    print("Area of Triangle:", area)

if __name__ == "__main__":

    print(("test program"))
    

