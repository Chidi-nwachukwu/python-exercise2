first_list = [2, 4, 6, 8,]
print(first_list)
first_list.append(10)
print(first_list)
first_list.insert(0, 99)
print(first_list)
first_list[0] += 1
print(first_list)
# to add another list to a list by concatenation
first_list += [7]
print(first_list)
# remove a number from the list
first_list.remove(10)
print(first_list)
# remove or pop an index in a list
first_list.pop(3)
print(first_list)
names = ("chidi","james","nonso","mofe")
names_joined = "*".join(names)
print(names_joined)
