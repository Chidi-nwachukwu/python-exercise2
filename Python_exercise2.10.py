# 2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.









number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
number3 = int(input("Enter third number"))

sum = number1 + number2 + number3
average = sum / 3
product = number1 * number2 * number3

maximum = number1
minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3



print("the sum is: ", sum);
print("the average is: ", average);
print("the product is: ", product);
print("the minimum number is:", minimum);
print("the maximum number is:", maximum);