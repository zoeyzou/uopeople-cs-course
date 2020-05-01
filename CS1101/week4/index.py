# def increment(x, y):
#     print(x + y)


# increment(1, "print")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# precondition in a function is being violated


def compare(x, y):
    if x > y:
        print(x + " is greater than " + y)
    elif x < y:
        print(x + " is less than " + y)


compare(1, 1)  # nothing is beng printed
# postcondition in a function is being voilated


def is_positive(x):
    return x > 0


num = is_positive(2)

reduced_num = num - 1

print(reduced_num)
