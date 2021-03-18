# Made by Snehashish Laskar!
# Made on 18-03-2021
# Developer contact: snehashish.laskar@gmail.com
# This is a mensuration calculator

""" 
    Intsructions:

    -> Please read the notes below before using this 


"""

# Create a class where all the area related functions are defined
class Area:

    def __init__(self):
        pass

    # Function to find the area of square
    def area_of_square(self):
        side = int(input("enter the side's measurement: "))
        self.area = side*side 
        print(f"self.area of square = {self.self.area}")

    def area_of_rectangle(self):
        length = int(input("enter the length: "))
        breadth = int(input("enter the breadth: "))
        self.area = length*breadth
        print(f"self.area of rectangle = {self.self.area}")

    def area_of_triangle(self):
        height = int(input("enter the height:"))
        base = int(input("enter the measurement of the base: "))
        self.area = (height*base)/2
        print(f"self.area of triangle = {self.self.area}")

    def area_of_parallelogram(self):
        height = int(input("enter the height of the parallelogram: "))
        breadth = int(input("enter the breadth of the parallelogram: "))
        self.area = breadth*height
        print(f"self.area ofparallelogram = {self.area}")

    def area_of_circle(self):
        radius = int(input("enter the radius of the circle: "))
        self.area = 3.14*(radius**2)
        print(f"self.area of circle = {self.area}")
    
    def area_of_rohmbus(self):
        diagonal1 = int(input("enter the first diagonal: "))
        diagonal2 = int(input("enter the second diagonal: "))
        self.area = (diagonal2*diagonal1)/2
        print(f"self.area of rohmbus = {self.area}")

    def area_of_trapezium(self, side1, side2, height):
        side1 = int(input("enter the measurement of the first side: "))
        side2 = int(input("enter the measurement of the second side: "))
        height  = int(input("enter the height of the trapezium: "))
        self.area = (height/2)*(side1+side2)
        print(f"self.area of trapezium = {self.area}")


class Perimeter:

    def __init__(self):
        pass

    def square(self):
        side = int(input("enter the measurement of the side: "))
        self.self.perimeter =  4*side
        print(f"Perimeter of square = {perimeter}")

    def rectangle(self):
        length = int(input("enter the length of the rectangle: "))
        breadth = int(input("enter the breadth of the rectangle: "))
        self.perimeter =  2*(length + breadth)
        print(f"Perimeter of rectangle = {perimeter}")

    def triangle(self, side1, side2, base):
        side1 = int(input("enter first side of the triangle: "))
        side2 = int(input("enter second side of the triangle: "))
        base = int(input("enter the base of the triangle: "))
        self.perimeter =  side1 + side2 + base
        print(f"Perimeter of triangle = {perimeter}")

    def parallelogram(self):
        length = int(input("enter the length of the parallelogram: "))
        breadth = int(input("enter the breadth of the parallelogram: "))
        self.perimeter =  2*(length + breadth)
        print(f"Perimeter of parallelogram = {perimeter}")

    def circumference_of_circle(self):
        radius = int(input("enter the radius of the circle: "))
        self.circumference = 2*(3.14*radius) 
        print(f"Circumference of circle = {circumference}")


class Volume:

    def __init__(self):
        pass

    def cube(self):
        side  = int(input("enter the side cube: "))
        self.volume = side**3 
        print(f"Volume of cube = {self.volume}")

    def cuboid(self):
        length = int(input("enter the length of the cuboid: "))
        base = int(input("enter the base of the cuboid: "))
        height = int(input("enter the height of the cuboid: "))
        self.volume = height*base*length
        print(f"Volume of cuboid = {self.volume}")

    def cylinder(self):
        height = int(input("enter the height of the cylinder: "))
        radius = int(input("enter the radius of the cylinder: "))
        self.volume = (3.14*(radius**2))*height
        print(f"Volume of cylinder = {self.volume}")

class Surface_area:

    def __init__(self):
        pass

    def cube(self):
        side = int(input("enter the side of the cube: "))
        self.surface_area = 6*(side**2)
        print(f"Surface area of cube = {self.surface_area}")

    def cuboid(self):
        length = int(input("enter the length of the cuboid: "))
        breadth = int(input("enter the breadth of the cuboid: "))
        self.surface_area =6*(length*breadth)
        print(f"Surface area of cuboid = {self.surface_area}")

class Lateral_Surface():

    def __init__(self):
        pass

    def Cube(self):
        side  = int(input("enter the side of the Cube: "))
        self.surface_area = 4*(side*side)
        print(f"Lateral Surface of cube= {self.surface_area}")

    def Cuboid(self, length, breadth, height):
        length = int(input("enter the length of the Cube: "))
        breadth = int(input("enter the breadth of the Cube: "))
        height = int(input("enter the height of the Cube: "))
        self.surface_area = height*(2*(length + breadth))
        print(f"Lateral Surface area of cuboid = {self.surface_area}")

    
Area = Area()
Perimeter = Perimeter()
Volume = Volume()
Surface_Area = Surface_area()
Lateral_Surface_Area = Lateral_Surface()
