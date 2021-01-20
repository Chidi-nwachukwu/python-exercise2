# 2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from the user.
# Display the sum, average, product, smallest and largest of the numbers. Note that each of these
# is a reduction in functional-style programming.

num1 = int(input("enter first_number:"))
num2 = int(input("enter second_number:"))
num3 = int(input("enter third_number:"))

sum = num1 + num2 + num3
average = num1 + num2 + num3 /3
product = num1 * num2 * num3
smallest = num1
largest = num1



if num1 + num2 + num3:
    print (sum, 'is the sum')

if num1 + num2 + num3 /3:
    print (average, 'is the average')

if num1 * num2 * num3:
    print(product, 'is the product')

if num2 > largest:
        largest = num2
if num2 < smallest:
        smallest = num2
if num3 > largest:
        largest = num3
if num3 < smallest:
        smallest = num3
print('Largest is ', largest, 'and smallest is', smallest)