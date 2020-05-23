def compare_lists(list_a, list_b):
    "given two lists, comparing them to see how many positions are matching"
    repeat_count = 0
    for a, b in zip(list_a, list_b):
        if a == b:
            repeat_count += 1
    return repeat_count


nums_a = [3, 6, 1, 8, 20, 4, 2, 3, 0]
nums_b = [6, 3, 1, 3, 7, 9, 24, 3, 2]
print(compare_lists(nums_a, nums_b))

my_dictionary = {"cute": "kawaii", "strange": "qiguai", "tasty": "haochi"}
for eng, other in my_dictionary.items():
    print(eng + " means " + other)


def get_users_info(user_dic):
    "takes in a dictionary, and return a list of tuples that include all the info in those dictionary items"
    users = []
    for first_name, last_name in user_dic:
        users.append((first_name, last_name, user_dic[first_name, last_name]))
    return users


user_dic = {("Zoey", "Zou"): "likes food", ("Denise", "Tham"): "likes food"}
print(get_users_info(user_dic))
