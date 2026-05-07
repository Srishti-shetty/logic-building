'''Program to Calculate the Area of a Circle and Triangle:
Write a program to calculate the area of a circle given its radius and a triangle
given its base and height. For example:
○ Input: Radius: 5, Base: 10, Height: 4
○ Output:Area of Circle: 78.5
Area of Triangle: 20'''

radius = float(input("Enter radius: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
circle_area = 3.14 * radius * radius
triangle_area = 0.5 * base * height
print("Area of Circle:", circle_area)
print("Area of Triangle:", triangle_area)