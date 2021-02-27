# let's collect an unknown number of student grades and find the average of the grades


# Algorithm
#     step 1
#         collect first student grade
#     step 2
#         initialize counter to zero
#     step 3
#         check if student grade is not a negative 1
#     step 4
#         keep collecting student grades
#     step 5
#         add student's grades
#     step 6
#         increment counter in the loop
#     step 7
#         calculate average of the total scores outside of the loop


user_input = int(input("enter student1 grade?"))
counter = 0
total = 0
while user_input >= 0:
    total = total + user_input
    counter += 1
    user_input = int(input(f"enter student{counter+1} grade?"))

average = total / counter
print("the average of the students is:", average)


