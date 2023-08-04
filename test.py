def circle():
    r = int(input("Enter the radius: "))
    area = r * r *3.14
    per = 2 * r *3.14
    print(f"area: {area} \nper: {per}")

circle()

def rectangle():
    m = int(input("Enter the first edge: "))
    n = int(input("Enter the second edge: "))
    area = m * n
    circumference = 2 * (m + n)
    print(f"area: {area} \ncircumference: {circumference}")

rectangle()


def triangle():
    b = int(input("Enter the base: "))
    h = int(input("Enter the height: "))
    e = int(input("Enter the third edge: "))
    area = 0.5 * (b * h)
    circumference = b + h + e
    print(f"area: {area} \ncircumference: {circumference}")

triangle()