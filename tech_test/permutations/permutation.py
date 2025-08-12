

# Problem Statement: String Permutations
# Problem Description
# Given a string, generate all possible permutations of its characters. A permutation is a rearrangement of the characters where each character appears exactly once.

# Examples:
# Input: "ab" → Output: ["ab", "ba"]
# Input: "abc" → Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
# Input: "aab" → Output: ["aab", "aba", "baa"]
# Requirements:
# Implement the most optimized solution possible
# Use appropriate data structures (no external libraries)
# Analyze time and space complexity
# Handle duplicate characters correctly
# Return results in lexicographical order (bonus)

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

# test = "abc"

# print(find_permutations(test))
