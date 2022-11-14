

def input_list():

    def create_user_input_list():
        while True:
            user_input_list.append(input())
            if user_input_list[-1] == "":
                break

    def find_sum_from_list(the_list):
        result = 0
        for x in the_list:
            result += x
        return result

    user_input_list = []
    create_user_input_list()
    user_input_list.pop(-1)
    floated_list = [float(x) for x in user_input_list]
    floated_list.append(find_sum_from_list(floated_list))
    return floated_list



def check_monotonic_sequence(sequence):
    mono = [False, False, False, False]
    compare_list = sequence.copy()
    reverse_compare_list = sequence.copy()
    set_list = set(sequence)
    compare_list.sort()
    reverse_compare_list.sort(reverse=True)
    if len(sequence) <= 1:
        return [True, True, True, True]
    elif compare_list == sequence and len(sequence) == len(set_list):
        mono[0] = True
        mono[1] = True
    elif compare_list == sequence:
        mono[0] = True
        if len(set_list) == 1:
            mono[2] = True
    elif reverse_compare_list == sequence and len(sequence) == len(set_list):
        mono[2] = True
        mono[3] = True
    elif reverse_compare_list == sequence:
        mono[2] = True
    return mono

def primes_generator(n):
    primes = []
    number = 2
    while len(primes) < n:
        for x in range(2, number):
            if number % x == 0:
                number += 1
                break
        else:
            primes.append(number)
            number += 1
    return primes

def check_monotonic_sequence_inverse(def_bool):
    match def_bool:
        case [True, True, False, False]:
            return [5, 9, 13, 15, 17, 30, 70, 200]
        case [True, False, True, False]:
            return [7, 7, 7, 7, 7]
        case [True, False, False, False]:
            return [5, 9, 9, 21]
        case [False, False, True, False]:
            return [16, 7, 3, 3]
        case [False, False, False, False]:
            return [9, -3, -1, 1]
        case [False, False, True, True]:
            return [11, 8, 7, 1]
        case [True,True,True,True]:
            return [69]
        case _:
            return None



def is_empty_vecotr(vec_lst):
    if len(vec_lst) == 0:
        return True
    else:
        return False

def vectors_list_sum(vec_lst):
    final_result = []
    for x in range(len(vec_lst[0])):
        amount = 0
        for y in range(len(vec_lst)):
            amount += vec_lst[y][x]
        final_result.append(amount)
    return final_result


def calc_the_inner_product(vec_1, vec_2):
    inner_product = 0
    if len(vec_1) == 0 and len(vec_2) == 0:
        return 0
    elif len(vec_1) == 0 or len(vec_2) == 0:
        return None
    for x in range(len(vec_1)):
        amount = vec_1[x] * vec_2[x]
        inner_product += amount
    return inner_product

def orthogonal_number(vectors):
    amount = 0
    for x in range(len(vectors)):
        for y in range(x + 1, len(vectors)):
            if calc_the_inner_product(vectors[x], vectors[y]) == 0:
                amount += 1
    return amount

########################
#         A. 1         #
########################

# Test manually


########################
#         A. 2         #
########################

assert calc_the_inner_product([1, 2, 3], [1, 2, 3]) == 14
assert calc_the_inner_product([1, 2, 3], [10.5, -2, 0]) == 6.5
assert calc_the_inner_product([1, 2, 3], []) is None
assert calc_the_inner_product([0], [0]) == 0
assert calc_the_inner_product([-10], [-5]) == 50
assert calc_the_inner_product([], [1]) is None
assert calc_the_inner_product([], []) == 0


########################
#         A. 3         #
########################

assert (check_monotonic_sequence([1, 2, 3, 4, 5, 6, 7, 8])
        == [True, True, False, False])

assert (check_monotonic_sequence([1, 2, 2, 3])
        == [True, False, False, False])

assert (check_monotonic_sequence([1, 1, 1, 1])
        == [True, False, True, False])

assert (check_monotonic_sequence([3, 2, 1, 1])
        == [False, False, True, False])

assert (check_monotonic_sequence([7.5, 4, 3.141, 0.111])
        == [False, False, True, True])

assert (check_monotonic_sequence([1, 0, -1, 1])
        == [False, False, False, False])

assert (check_monotonic_sequence([])
        == [True, True, True, True])

assert (check_monotonic_sequence([100])
        == [True, True, True, True])

assert (check_monotonic_sequence([-10])
        == [True, True, True, True])

assert (check_monotonic_sequence([0])
        == [True, True, True, True])


########################
#         A. 4         #
########################

bool_def = [True, True, False, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [False, False, True, True]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [True, False, True, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [True, False, False, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [False, False, True, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [False, False, False, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [True, True, True, True]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def
assert len(check_monotonic_sequence_inverse(bool_def)) <= 1


bool_def = [False, True, False, False]
assert check_monotonic_sequence_inverse(bool_def) is None

bool_def = [False, False, False, True]
assert check_monotonic_sequence_inverse(bool_def) is None




bool_def = [False, True, True, False]
assert check_monotonic_sequence_inverse(bool_def) is None

bool_def = [True, False, False, True]
assert check_monotonic_sequence_inverse(bool_def) is None


########################
#         A. 5         #
########################

assert primes_generator(0) == []
assert primes_generator(1) == [2]
assert primes_generator(2) == [2, 3]
assert primes_generator(7) == [2, 3, 5, 7, 11, 13, 17]
assert primes_generator(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                                89, 97, 101, 103, 107, 109, 113, 127, 131,
                                137, 139, 149, 151, 157, 163, 167, 173, 179,
                                181, 191, 193, 197, 199, 211, 223, 227, 229]


########################
#         A. 6         #
########################

assert vectors_list_sum([[1, 1], [1, 3]]) == [2, 4]

assert vectors_list_sum([[1, 1, 1], [1, 0, 0], [0, 0, 100]]) == [2, 1, 101]

assert vectors_list_sum([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [2, 2, 2, 2, 2]


########################
#         A. 6         #
########################

assert orthogonal_number([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

assert orthogonal_number([[0, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

assert orthogonal_number([[0, 0], [1, 2], [10, 5]]) == 2

assert orthogonal_number([[1, 1, 1, 1],
                          [2, 1, 3, 3],
                          [0, 0, 100, 33],
                          [8, 8, 8, 1.5],
                          [9, 9, 9, 9]]) == 0

assert orthogonal_number([[0], [0], [0], [0]]) == 6

print("All tests passed")

