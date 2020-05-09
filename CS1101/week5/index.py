# Part 1
# Encapsulate the following Python code from Section 7.5 in a function named my_sqrt that takes a as a parameter, chooses a starting value for x, and returns an estimate of the square root of a.
def my_sqrt(a):
    if a < 1:
        a = 1  # a safety guard if passed in argument is 0

    x = a  # initiate x with value of a
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return x


# Part 2
# Write a function named test_sqrt that prints a table like the following using a while loop, where "diff" is the absolute value of the difference between my_sqrt(a) and math.sqrt(a).
def test_sqrt():
    a = 1  # the program start from 1, and this a is a counter
    while a <= 25:  # program should exit while loop when a is greater than 25
        import math

        # assign the values to variable so no need to repeat in the following code
        x = my_sqrt(a)
        y = math.sqrt(a)
        print(
            "a = "
            + str(a)  # need to stringify the int to avoid type error
            + " | "
            + "my_sqrt(a) = "
            + str(x)
            + " | "
            + "math.sqrt(a) = "
            + str(y)
            + " | "
            + "diff = "
            + str(abs(x - y))
        )
        a = a + 1  # increment the counter by 1


test_sqrt()
