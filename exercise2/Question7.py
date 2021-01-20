#2.7 (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and whether 2 is a
# multiple of 10. (Hint: Use the remainder operator.)

num = int(input('enter a num!'))
multiples = int(input("enter a multiple num!"))

if num % multiples == 0:
    print(num, 'is a multiple of:', multiples)
# else:
#     print(num, 'is not a multiple of', multiples)