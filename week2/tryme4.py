# Provided by the assignment
def new_line():
    print(".")


# Provided by the assignment
def three_lines():
    new_line()
    new_line()
    new_line()


# Create a function that uses `three_lines` to print nine lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()


# Create a function use a combination of above and print 25 lines
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()


nine_lines()
print("------ calling next function ------")  # to separate two function calls
clear_screen()
