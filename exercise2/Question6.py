#2.6 (Odd or Even) Use if statements to determine whether an integer is odd or even. [Hint: Use the
# remainder operator. An even number is a multiple of 2. Any multiple of 2 leaves a remainder of 0 when
# divided by 2.]


number1 = int(input('determine if number is odd or even:'))
if(number1 %2) == 0:
    print("{0} is Even number".format(number1))