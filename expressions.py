

import math

def calc_math_expression(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2#
    elif operator == "*":
        return num1 * num2
    elif operator == ":" and num2 != 0:
        return num1 / num2
    else:
       return None


def calc_math_expression_from_str(str_input):
     my_list = str_input.split()
     operator = my_list[1]
     num1 = float(my_list[0])
     num2 = float(my_list[2])
     return calc_math_expression(num1, num2, operator)


def find_largest_and_smallest_numbers(num1=52, num2=35, num3=12):
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    elif num3 >= num2 and num3 >= num1:
        largest = num3
    if num1 <= num2 and num1 <= num3:
        smallest = num1
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
    elif num3 <= num2 and num3 <= num1:
        smallest = num3
    numbers = (largest, smallest)
    return numbers

def quadratic_equation_solver(a, b, c):
    try:
        x = (-b + math.sqrt((b ** 2) - (4 * a * c)))/(2*a)
        y = (-b - math.sqrt((b ** 2) - (4 * a * c)))/(2*a)
    except:
        return (None, None)
    if ((b ** 2) - (4 * a * c)) == 0:
        return (x, None)
    else:
        return (x,y)

def quadratic_equation_solver_from_user_input():
    user_input = input("Enter a number string: ")
    numbers = user_input.split()
    numbers = [float(x) for x in numbers]
    if numbers[0] == 0 or len(numbers) != 3:
        print(" A cannot be zero AND you must only input 3 numbers")
    else:
        return quadratic_equation_solver(numbers[0], numbers[1], numbers[2])

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if temp_1 > min_temp:
        if temp_2 > min_temp:
            return True
        elif temp_3 > min_temp:
            return True
        else:
            return False
    elif temp_2 > min_temp and temp_3 > min_temp:
        return True
    else:
        return False

assert calc_math_expression_from_str("10 : 2") == 5.0
assert calc_math_expression_from_str("10 : -2") == -5.0
assert calc_math_expression_from_str("-10 : -2") == 5.0
assert calc_math_expression_from_str("-10 : 2") == -5.0
assert calc_math_expression_from_str("10 + 2") == 12.0
assert calc_math_expression_from_str("100 - 39.3") == 60.7
assert calc_math_expression_from_str("5 : 2") == 2.5
assert calc_math_expression_from_str("5 : 0") is None
assert calc_math_expression_from_str("10 333 2") is None
assert calc_math_expression_from_str("10 ^ 2") is None


assert find_largest_and_smallest_numbers(5, 1, 10) == (10, 1)
assert find_largest_and_smallest_numbers(2.5, 2.5, 7) == (7, 2.5)
assert find_largest_and_smallest_numbers(7, 2.5, 2.5) == (7, 2.5)
assert find_largest_and_smallest_numbers(-5, -5, -5) == (-5, -5)
assert find_largest_and_smallest_numbers(10, -1, 10) == (10, -1)
assert find_largest_and_smallest_numbers(-2, 5, -2) == (5, -2)
assert find_largest_and_smallest_numbers(3, 20, -2) == (20, -2)
assert find_largest_and_smallest_numbers(7, 10, 0) == (10, 0)
assert find_largest_and_smallest_numbers(10, 7, 0) == (10, 0)
assert find_largest_and_smallest_numbers(0, 10.01, 10) == (10.01, 0)

assert quadratic_equation_solver(1, 1.5, -1) == (0.5, -2)
assert quadratic_equation_solver(1, -8, 16) == (4, None)
assert quadratic_equation_solver(1, -2, 34.5) == (None, None)
assert quadratic_equation_solver(4, -12, 9) == (3/2, None)


assert temp_checker(26, 38, 90, 20) is True
assert temp_checker(10, 10, 10, 10) is False
assert temp_checker(10, 11, 10, 11) is True
assert temp_checker(-1, -9, 0, 1) is True
assert temp_checker(0, 90, 0, 1) is True

print("All tests passed")



