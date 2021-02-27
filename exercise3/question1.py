# 3.1 (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any
# input, if the value entered is other than 1 or 2, keep looping until the user enters a correct
# value. Use one counter to keep track of the number of passes, then calculate the number
# of failures after all the user’s inputs have been received.

fail = 0
passed = 0
counter = 1

while counter <= 10:
    x=int(input("enter a number"))
    if x == 1:
        passed += 1

    else:
        fail +=1

    counter +=1
print(passed)
print(fail)