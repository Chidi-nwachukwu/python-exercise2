# A college offers a course that prepares students for the state licensing exam for realestate brokers. Last year, several of the students who completed this course took the
# licensing examination. The college wants to know how well its students did on the
# exam. You have been asked to write a program to summarize the results. You have
# been given a list of these 10 students. Next to each name is written a 1 if the student passed the exam and a 2 if the student failed.
# Your program should analyze the results of the exam as follows:
# 1. Input each test result (i.e., a 1 or a 2). Display the message “Enter result”
# each time the program requests another test result.
# 2. Count the number of test results of each type.
# 3. Display a summary of the test results indicating the number of students who
# passed and the number of students who failed.
# 4. If more than eight students passed the exam, display “Bonus to instructor.”



passes = 0
failures = 0

for students in range (10):
    result = int(input("enter result (1=pass, 2=fail): "))

    if result == 1:
        passes += 1

    else:
        failures += 1

        print(f'the number of failures is {failures}')
        print(f'the number of passes is {passes}')

    if passes > 8:
        print("Bonus to instructor")

