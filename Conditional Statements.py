def check_area(area):
    print(f"area is {area}")
    if area > 10:
        print("area is bigger than 10\n")
    elif area == 10:
        print("area is equal to 10\n")
    elif area < 10 and area > 0:
        print("area is smaller than 10")
    else:
        print("Invalid value")
def circle(raduis):
    area= (raduis ** 2) * 3.14
    check_area(area)
def triangle(base , height):
    area = 0.5 * base * height
    check_area(area)

def rectangle(length , width):
    area= length * width
    check_area(area)

e = int(input("Enter the edge : "))
h = int(input("Enter the height : "))
b = int(input("Enter the base : "))
triangle(2 , 10)

r = float(input("Enter the raduis : "))
circle(2)

w = int(input("Enter the wight : "))
h = int(input("Enter the height : "))
rectangle(4 , 2)