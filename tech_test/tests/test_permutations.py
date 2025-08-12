import pytest
import math
# from permutations.permutation import find_permutations

def find_permutations(string):

    if(len(string) == 1):
        return [string]

    permutations = [""]
    for char in string:

        new_permutations = []
        for perm in permutations:

            # Loops through each current permutation
            for i in range(len(perm) + 1):
                # left of current character
                left = perm[:i]
                # right of current character
                right = perm[i:]

                # add character in between each position
                new_permutations.append(left + char + right)

            permutations = new_permutations

    # Return only unique permutations
    unique = set(permutations)
    # Sort alphabetically
    sorted_perm = sorted(unique)
    return sorted_perm

def test_empty_string():
    assert find_permutations("") == [""]

def test_empty_string():
    assert find_permutations("") == [""]

def test_single_character():
    assert find_permutations("a") == ["a"]

def test_two__characters():
    test_string = "ab"
    result = find_permutations(test_string)
    expected = ["ab", "ba"]
    assert sorted(result) == sorted(expected)

def test_three__characters():
    test_string = "abc"
    result = find_permutations(test_string)
    expected = ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert sorted(result) == sorted(expected)

def test_duplicate_characters():
    test_string = "aab"
    result = find_permutations(test_string)
    expected_set = ["aab", "aba", "baa"]
    assert result == expected_set

def test_length_of_permutations():
    test_string = "abcd"
    result = find_permutations(test_string)
    assert len(result) == math.factorial(len(test_string))  # 4! = 24