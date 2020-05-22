# Create a string that is a long series of words separated by spaces. The string is your own creative choice. It can be names, favorite foods, animals, anything. Just make it up yourself.

delicious_food = "fried_noodle dim_sum pasta sushi tepanyaki tom_yum"

# Turn the string into a list of words using split.

food_list = delicious_food.split(" ")
print(
    food_list
)  # output: ['fried_noodle', 'dim_sum', 'pasta', 'sushi', 'tepanyaki', 'tom_yum']

# Delete three words from the list, but delete each one using a different kind of Python operation.

food_list.pop()  # without giving index, pop removes the last item
print(food_list)  # output: ['fried_noodle', 'dim_sum', 'pasta', 'sushi', 'tepanyaki']

food_list.remove("pasta")  # if you know which item you want to remove
print(food_list)  # output: ['fried_noodle', 'dim_sum', 'sushi', 'tepanyaki']

del food_list[2]
print(food_list)  # output: ['fried_noodle', 'dim_sum', 'tepanyaki']

# Sort the list

food_list.sort()
print(food_list)  # output: ['dim_sum', 'fried_noodle', 'tepanyaki']

# Add new words to the list (three or more) using three different kinds of Python operation.

food_list.append("hot_pot")
print(food_list)  # output: ['dim_sum', 'fried_noodle', 'tepanyaki', 'hot_pot']

food_list.extend(["fried_rice"])
print(
    food_list
)  # output: ['dim_sum', 'fried_noodle', 'tepanyaki', 'hot_pot', 'fried_rice']

food_list.insert(
    0, "dumpling"
)  # insert requires an index and value to add item to specific location of the list
print(
    food_list
)  # output: ['dumpling', 'dim_sum', 'fried_noodle', 'tepanyaki', 'hot_pot', 'fried_rice']

# Turn the list of words back into a single string using join & Print the string
delimiter = " "
food_list = delimiter.join(food_list)
print(food_list)  # output: "dumpling dim_sum fried_noodle tepanyaki hot_pot fried_rice"


def get_odd_numbers(r):
    "A function that loops through a number range and get the odd numbers, return them in a list"
    number_list = []
    for i in range(r):
        if i % 2 != 0:
            number_list.append(i)
    return number_list


print(get_odd_numbers(10))

# A list operation that is legal but does the "wrong" thing, not what the programmer expects
def get_sorted_food_list(food_list):
    "A function that takes in a list of food, filter it and sort it"
    filtered_list = []

    for item in food_list:
        if item.find("food") > -1:
            filtered_list.append(item)
    sorted_food_list = filtered_list.sort()

    return sorted_food_list


print(get_sorted_food_list(["yummy food", "grass", "sweet food"]))
y = [2]
z = y
print(id(y), id(z))
print(y is z)
x = list(z)
print(x)
