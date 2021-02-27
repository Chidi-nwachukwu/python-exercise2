from exercise3.utils import multiply,addition
user1 = input("enter a celcius of your choice seperated by a comma:")

def celcius_to_fahrenheit(temperature):
     fahrenheit = addition(32,multiply(temperature,1.8))
     return fahrenheit

user1_list = user1.split(",")
print("temperature", user1_list)

for user2 in user1_list:
     temp = float(user2)
     fahrenheit = celcius_to_fahrenheit(temp)
     print(fahrenheit)










# number = 0
# counter = 1
#
# for user1 in range(0, 10):
#
# #      counter+= 1
# #      print(user1)
# for user1 in user1:
#




