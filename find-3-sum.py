"""
given an array of numbers
a: [-5, -2, 0, -1, 1, 1, 4]
find groups of 3 numbers having sum of 0
expected result: [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]]
"""


def find_3_sum(array: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    array.sort()

    for i in range(0, len(array) - 2):
        # skip array[i] value if previous value is the same
        # since we already processed it and found all possible combinations
        if i > 0 and array[i] == array[i - 1]:
            continue

        j = i + 1  # left pointer
        k = len(array) - 1  # right pointer

        # search for remaining 2 numbers until left and right pointers collide
        while j < k:
            value1 = array[i]
            value2 = array[j]
            value3 = array[k]
            sum = value1 + value2 + value3
            if sum == 0:
                result.append([value1, value2, value3])
                j += 1
                # since we found a match, if 2nd number (j) is the same as previous, skip
                # with constraint that j is still less than k index
                while j < k and array[j] == array[j - 1]:
                    j += 1
            elif sum < 0:
                j += 1
            elif sum > 0:
                k -= 1

    return result


def are_arrays_equal(array1: list[int], array2: list[int]) -> bool:
    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False

    return True


def run_test(array: list[int], expected: list[list[int]]):
    actual = find_3_sum(array)
    if are_arrays_equal(actual, expected):
        print(f"PASS: {array} => {actual}")
    else:
        print(f"FAIL: {array} => {actual} (expected: {expected})")


run_test([-5, -2, 0, -1, 1, 1, 4], [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]])
run_test([0, 0, 0, 0], [[0, 0, 0]])
run_test([0, 1, 2, 3], [])
# corner cases
run_test(
    [-5, -5, -4, -4, 0, 1, 1, 4, 4, 2, 2, 3, 3],
    [[-5, 1, 4], [-5, 2, 3], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2]],
)

"""
Output
PASS: [-5, -2, -1, 0, 1, 1, 4] => [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]]
PASS: [0, 0, 0, 0] => [[0, 0, 0]]
PASS: [0, 1, 2, 3] => []
PASS: [-5, -5, -4, -4, 0, 1, 1, 2, 2, 3, 3, 4, 4] => [[-5, 1, 4], [-5, 2, 3], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2]]
"""
