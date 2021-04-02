# function with multiple parameters
# maximum of three values....

def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    print( max_value)



maximum('Banana', 'Apple', 'Orange')
