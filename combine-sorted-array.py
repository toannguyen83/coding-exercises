"""
given 2 sorted array
a [4, 5, 7, 9]
b [-2, 0, 2, 3, 5]

create a function that can return the the 2 arrays merged and also sorted
from above result, expected value is [-2, 0, 2, 3, 4, 5, 5, 7, 9]
"""


def combine_sorted_arrays(array_a: list[int], array_b: list[int]) -> list[int]:
    result: list[int] = []

    a_index = 0
    b_index = 0

    while a_index < len(array_a) and b_index < len(array_b):
        a_value = array_a[a_index]
        b_value = array_b[b_index]

        if a_value < b_value:
            result.append(a_value)
            a_index += 1
        else:
            result.append(b_value)
            b_index += 1

    if a_index < len(array_a):
        result.extend(array_a[a_index:])
    elif b_index < len(array_b):
        result.extend(array_b[b_index:])

    return result


def run_test(a: list[int], b: list[int], expected: list[int]):
    actual = combine_sorted_arrays(a, b)
    if actual == expected:
        print(f"PASS: {a} + {b} => {actual}")
    else:
        print(f"FAIL: {a} + {b} => {actual} (expected: {expected})")


run_test([4, 5, 7, 9], [-2, 0, 2, 3, 5], [-2, 0, 2, 3, 4, 5, 5, 7, 9])
run_test([1], [0], [0, 1])
run_test([7, 15, 18, 20], [-2, 0], [-2, 0, 7, 15, 18, 20])
run_test([4, 5, 7, 9], [-2, 0, 2, 3, 5], [-2, 0, 2, 3, 4, 5, 5, 7, 9])

"""
Output: 
PASS: [4, 5, 7, 9] + [-2, 0, 2, 3, 5] => [-2, 0, 2, 3, 4, 5, 5, 7, 9]
PASS: [1] + [0] => [0, 1]
PASS: [7, 15, 18, 20] + [-2, 0] => [-2, 0, 7, 15, 18, 20]
PASS: [4, 5, 7, 9] + [-2, 0, 2, 3, 5] => [-2, 0, 2, 3, 4, 5, 5, 7, 9]

Complexity:
O(n + m) where n is len of array a, and m is len of array b
"""
