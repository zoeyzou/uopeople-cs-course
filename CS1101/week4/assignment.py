# Function from text book
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


# exercise: A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case
def is_power(x, y):
    if not is_divisible(x, y):  # early check if it's not divisible
        return False
    elif x == y:  # base case
        return True
    elif y == 1:  # only 1 is to the power of 1
        return x == 1
    else:
        return is_power(x / y, y)  # recursively dividing parameter x


# test cases
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
