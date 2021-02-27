# 2.11 (Separating the Digits in an Integer) Write a script that
# inputs a five-digit integer from the user. Separate the number into
# its individual digits. Print them separated by three spaces each. For
# example, if the user types in the number 42339, the script should print
# 4   2   3   3   9 Assume that the user enters the correct number of
# digits. Use both the floor division and remainder operations to
# “pick off” each digit.
number = int(input("enter the integer"))
number1 = number // 10000
number2 = number % 10000
number3 = number2 // 1000
number4 = number2 % 1000
number5 = number4 // 100
number6 = number4 % 100
number7 = number6 // 10
number8 = number6 % 10

print(number1,"", number3,"", number5,"", number7,"" ,number8)