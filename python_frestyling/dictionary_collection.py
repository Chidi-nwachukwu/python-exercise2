# return a dictionary with squares as the keys and the square value of the values as the values
squares = ["one", "two", "three", "four", "five"]
values = [1, 2, 3, 4, 5]

def number_square(squares, values):
    squares1 = {}
    for x, y in zip(squares, values):
        squares1[x] = y **2
    return squares1
def main():
    print(number_square(squares, values))

main()