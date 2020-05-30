def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if not isinstance(val, list):
            val = [
                d[key]
            ]  # check if the value is list, if not convert it into list so it can be looped
        for item in val:
            if item not in inverse:
                inverse[item] = [key]
            else:
                inverse[item].append(key)
    return inverse


import ast

with open("original.txt") as original:
    content = original.read()  # this method will read the input as string

    dictionary = ast.literal_eval(content)  # convert str to dictionary
    dictionary["enjoy_weekend"] = True  # add three keys
    dictionary["work_experience"] = 2
    dictionary["friends"] = ["Denise", "Chloe", "Fion"]
    dictionary = invert_dict(dictionary)  # invert it


with open("output.txt", "w") as output:
    output.write(
        "%s" % dictionary
    )  # with format operator %s the dictionary will be formatted as string
