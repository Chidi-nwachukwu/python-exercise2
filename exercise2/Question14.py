def calculate_max_heart_rate(age: int):
    max_heart_rate = 220 - age
    return max_heart_rate


def calculate_target_heart__rate(age: int):
    max_target_rate = (50 * calculate_max_heart_rate(age)/100)
    min_target_rate = (85 * calculate_max_heart_rate(age)/100)
    print(f"for your age {age}, your Maximum Heart Rate is {calculate_max_heart_rate(age),} with your minimum Target Rate:{max_target_rate}")


def main():
    age = int(input("Please Enter Your Age, To Get Maximum Target Rate: "))
    calculate_target_heart__rate(age)


if __name__ == '__main__':
    main()

