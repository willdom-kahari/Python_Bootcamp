#add two numbers
def add_numbers(summand, addend):
    return summand + addend

# subtract the subtrahend from the minuend
def subtract_numbers(minuend, subtrahend):
    return minuend - subtrahend

# multiply two numbers
def multiply_numbers(multiplier, multiplicand):
    return multiplier * multiplicand

# divide the dividend by the divisor and handle exceptions
def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "None"

# validate numbers
def validate(num_input):
    try:
        num_input = int(num_input)
    except ValueError:
        num_input = __validate_internal(num_input)
    return num_input


def __validate_internal(num_input):
    try:
        print(f"{num_input} is not an integer")
        num_input = int(input(f"Re-enter an integer value: "))
    except ValueError:
        num_input = __validate_internal(num_input)
    return num_input

# define list of numbers
num_list = []

# collect only 3 values
for num in range(3):
    input_int = input(f"Enter integer value {num + 1}: ")
    list_item = validate(input_int)
    num_list.append(list_item)

#ask user to enter manipulating value
manipulating_int = input(f"Enter the value of an integer to manipulate the previously entered numbers: ")
valid_manipulator = validate(manipulating_int)

#print the results
for num in num_list:
    print("\n============================================")
    print(f"The result of adding {num} and {valid_manipulator} is {add_numbers(num, valid_manipulator)}")
    print(f"The result of subtracting {valid_manipulator} from {num} is {subtract_numbers(num, valid_manipulator)}")
    print(f"The result of multiplying {num} by {valid_manipulator} is {multiply_numbers(num, valid_manipulator)}")
    print(f"The result of dividing {num} by {valid_manipulator} is {divide_numbers(num, valid_manipulator)}")
