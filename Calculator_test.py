from Calculator import *

def run_test():
    """test all the functions"""
    assert add(2, 3) == 5, "2 + 3 is 5"
    assert subtract(2, 3) == -1, "2 - 3 is -1"
    assert multiply(2, 3) == 6, "2 * 3 is 6"
    assert division(6, 3) == 2, " 6 / 3 is 2"
    assert  square_root(9) == 3, "square_root of 9 is 3"
    assert square(2) == 4, "square of two is 4"

if __name__ == "_main_":
    run_test()