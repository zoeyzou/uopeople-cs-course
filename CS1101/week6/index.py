# Part 1
delicious_food = "fried_noodle dim_sum pasta sushi tepanyaki tom_yum"
food_list = delicious_food.split(" ")
print(food_list)

food_list.pop()
print(food_list)

food_list.remove("pasta")
print(food_list)

del food_list[2]
print(food_list)

food_list.sort()
print(food_list)
