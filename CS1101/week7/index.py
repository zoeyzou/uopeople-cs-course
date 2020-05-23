alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]

test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# Part 1

# Write a function called has_duplicates that takes a string parameter and returns True if the string has any repeated characters. Otherwise, it should return False.

# Implement has_duplicates by creating a histogram using the histogram function above. Do not use any of the implementations of has_duplicates that are given in your textbook. Instead, your implementation should use the counts in the histogram to decide if there are any duplicates.

# Write a loop over the strings in the provided test_dups list. Print each string in the list and whether or not it has any duplicates based on the return value of has_duplicates for that string. For example, the output for "aaa" and "abc" would be the following.

# aaa has duplicates
# abc has no duplicates

# Print a line like one of the above for each of the strings in test_dups.


def has_duplicates(str):
    histo = histogram(str)

    for char in histo:  # loop through every entry in the dictionary
        if histo[char] > 1:  # access the value to see if any character repeats
            return True

    return False


for item in test_dups:
    if has_duplicates(item):
        print(item, "has duplicates")
    else:
        print(item, "has no duplicates")

print("------------------------- separator ----------------------------")

# Part 2

# Write a function called missing_letters that takes a string parameter and returns a new string with all the letters of the alphabet that are not in the argument string. The letters in the returned string should be in alphabetical order.

# Your implementation should use a histogram from the histogram function. It should also use the global variable alphabet. It should use this global variable directly, not through an argument or a local copy. It should loop over the letters in alphabet to determine which are missing from the input parameter.

# The function missing_letters should combine the list of missing letters into a string and return that string.

# Write a loop over the strings in list test_miss and call missing_letters with each string. Print a line for each string listing the missing letters. For example, for the string "aaa", the output should be the following.

# aaa is missing letters bcdefghijklmnopqrstuvwxyz

# If the string has all the letters in alphabet, the output should say it uses all the letters. For example, the output for the string alphabet itself would be the following.

# abcdefghijklmnopqrstuvwxyz uses all the letters

# Print a line like one of the above for each of the strings in test_miss.


def missing_letters(str):
    global alphabet

    histo = histogram(str)
    alphabet_list = list(alphabet)

    for char in histo:
        if char in alphabet_list:
            alphabet_list.remove(char)  # remove the characters from the alphabet list

    return ("").join(alphabet_list)  # join all the characters into a string


for str in test_miss:
    missing = missing_letters(str)

    if len(missing) == 0:
        print(str, "uses all the letters")
    else:
        print(str, "is missing letters", missing)
