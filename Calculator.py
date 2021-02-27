def add (num1: float, num2: float) -> float:

    """a function that adds two numbers"""
    # logic here
    num3 = num1 + num2
    return num3

def multiply (num1: float, num2: float) -> float:

    """a function that multiplies two numbers"""
    # logic here
    num3 = num1 * num2
    return num3

def subtract (num1: float, num2: float) -> float:

    """a function that subtracts two numbers, num1 - num2"""
    # logic here
    num3 = num1 - num2
    return num3


def division (num1: float, num2: float) -> float:

    """a function that divides two numbers, num1 divides num2"""
    # logic here
    num3 = num1 / num2
    return num3


def square_root (num1: float) -> float:

    """a function that returns the square root of a number"""
    # logic here
    num2 = num1 ** 0.5
    return num2


def square(num1: float) -> float:

    """a function that returns a square of a number"""
    # logic here
    num2 = num1 ** 2
    return num2

def run_test():
    """test all the functions"""
    assert add(2, 3) == 5, "2 + 3 is 5"
    assert subtract(2, 3) == -1, "2 - 3 is -1"
    assert multiply(2, 3) == 6, "2 * 3 is 6"
    assert division(6, 3) == 2, " 6 / 3 is 2"
    assert  square_root(9) == 3, "square_root of 9 is 3"
    assert square(2) == 4, "square of two is 4"

def main():
    # run all the test
    print("running test......")
    run_test()
    print("all test passed")

    # add two numbers
    x = 2
    y = 10
    z = add(x, y)
    print(f"x + y: {x} + {y} = {z}")
    
if __name__ =="_main_":
    main()