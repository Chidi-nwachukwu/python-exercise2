#2.5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter,
# circumference and area. Use the value 3.14159 for π. Use the following formulas (r is the radius):
# diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll introduce Python’s math
# module which contains a higher-precision representation of π.]
#diameter = 2 * 2,   circumference = 2 * 3.14 * 2,diameter = 2 * 2,   circumference = 2 * 3.14 * 2,diameter = 2 * 2,


radius = float(input('enter the radius of the circle:'))
area = 3.14 * radius ** 2
diameter = 2* radius
circumference = 2*3.14159* radius

print("area of the circle is: ", area)
print('the circumference is: ', circumference)
print('the diameter is:, ', diameter)