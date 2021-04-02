

# write a for loop that collects from user input,the group number as key
# and a list of the member names as the values
# and then returns a dictionary of the entire collection

example:{ 1: ["dotun", "mofe", "nonso",], 2:["titus", "dami", "chidi"] }

def entire_collection():
    ds_group_collection = {}
    for i in range(3):
      x = int(input("enter your group_number:"))
      y = str(input("Enter your group_members:"))
      ds_group_collection[x] = y
    return (ds_group_collection)


def main():
   my_group = entire_collection()
   print(my_group)

main()