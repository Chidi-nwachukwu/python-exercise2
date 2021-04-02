# Write a function that takes a list of Python objects. Sum the objects that either
# are integers or can be turned into integers, ignoring the others.

objects_list = ['chidi', 2, 4, 3, 'miracle',1, 'orange']
def my_sum(numbers):
    new_list = []
    try:
        new_list = [num for num in numbers if isinstance(num, int)]
    except TypeError:
        pass
    new_list.sort()
    print(new_list)
    return sum(new_list)

print(my_sum(objects_list))
